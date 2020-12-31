from rest_framework import serializers
from mini_wallet.core.models import UserWallet, UserTransaction
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class WalletSerializer(serializers.ModelSerializer):
    status_wallet = serializers.SerializerMethodField(method_name='conversion_bool')

    class Meta:
        model = UserWallet
        fields = ('id',
                  'user',
                  'balance',
                  'status_wallet',
                  'disabled_at')


    def update(self, instance, validated_data):
        if self.initial_data.get('is_disabled','') == 'true' or self.initial_data.get('is_disabled','') == 'True':
            stat_value = True
        elif self.initial_data.get('is_disabled','') == 'false' or self.initial_data.get('is_disabled','') == 'False':
            stat_value = False
        else:
            stat_value = self.initial_data.get('is_disabled','')

        instance.status_wallet = stat_value
        instance.save()
        return instance


    def conversion_bool(self, instance):
        if instance.status_wallet:
            return "Disabled"
        else:
            return "Enabled"


    def validate(self, data):
        self.get_val = True
        if self.initial_data.get('is_disabled', '') == 'true' or self.initial_data.get('is_disabled', '') == 'True':
            initial_data = True
        elif self.initial_data.get('is_disabled', '') == 'false' or self.initial_data.get('is_disabled', '') == 'False':
            initial_data = False
        else:
            initial_data = None

        if initial_data is not None and initial_data == self.instance.status_wallet:
            if initial_data:
                status = "Disabled"
            else:
                status = "Enabled"
            raise serializers.ValidationError("Already " + status)
        elif initial_data is None:
            if self.instance.status_wallet:
                self.initial_data['is_disabled'] = False
            else:
                raise serializers.ValidationError("Already Enabled")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email',)

    def to_representation(self, instance):
        UserWallet.objects.create(balance=0, status_wallet=True, user_id=instance.id)
        token = Token.objects.create(user=instance)
        return {
            'token' : token.key
        }


class UserDepositTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTransaction
        fields = ('id','deposited_by','status_transaction','deposited_at','amount','reference_id')


    def create(self, validated_data):
        try:
            userid = self.initial_data['user']
            userwallet = UserWallet.objects.get(user_id=userid)
            validated_data['userwallet_id'] = userwallet.id
            validated_data['status_transaction'] = 'success'
            validated_data['deposited_by'] = userid
            validated_data['type_transaction'] = 'Deposit'
            instance = UserTransaction(**validated_data)
            instance.save()

            userwallet.balance = userwallet.balance + instance.amount
            userwallet.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError('Error on Deposit Amount : '+ str(e))


    def validate(self,data):
        userwallet = UserWallet.objects.get(user_id=self.initial_data.get('user',1))
        if userwallet.status_wallet:
            raise serializers.ValidationError('Disabled')
        return data


class UserWithdrawTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTransaction
        fields = ('id','deposited_by','status_transaction','deposited_at','amount','reference_id')


    def create(self, validated_data):
        try:
            userid = self.initial_data['user']
            userwallet = UserWallet.objects.get(user_id=userid)
            validated_data['userwallet_id'] = userwallet.id
            validated_data['status_transaction'] = 'success'
            validated_data['deposited_by'] = userid
            validated_data['type_transaction'] = 'Withdraw'
            instance = UserTransaction(**validated_data)
            instance.save()

            userwallet.balance = userwallet.balance - instance.amount
            userwallet.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError('Error on Withdraw Amount : '+ str(e))


    def validate(self,data):
        userwallet = UserWallet.objects.get(user_id=self.initial_data.get('user',1))
        if userwallet.status_wallet:
            raise serializers.ValidationError('Disabled')

        if userwallet.balance < data.get('amount'):
            raise  serializers.ValidationError('Not Enough Balance')
        return data