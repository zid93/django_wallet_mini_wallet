from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from mini_wallet.core.serializers import UserSerializer, WalletSerializer, UserDepositTransactionSerializer, UserWithdrawTransactionSerializer
from mini_wallet.core.models import UserWallet
from django.http.response import JsonResponse

# Create your views here.

class initAccount(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'data': serializer.data,'status': 'success'}
            return JsonResponse(data)
        else:
            data = {'data': {'error': serializer.errors},'status': 'fail'}
            return JsonResponse(data)


class statusWallet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        userid = request.POST.get('user', 1)
        wallet = UserWallet.objects.get(user_id=userid)
        wallet_serializer = WalletSerializer(wallet, data=request.data)
        if wallet_serializer.is_valid():
            wallet_serializer.save()
            data = {'data': {'data': {'wallet': wallet_serializer.data}},'status': 'success'}
            return JsonResponse(data)
        else:
            data = {'data': wallet_serializer.errors,'status': 'Failed'}
            return JsonResponse(data)

    def patch(self, request):
        userid = request.POST.get('user', 1)
        wallet = UserWallet.objects.get(user_id=userid)
        wallet_serializer = WalletSerializer(wallet,data=request.data, partial=True)
        if wallet_serializer.is_valid():
            wallet_serializer.save()
            data = {'data': {'data': {'wallet' : wallet_serializer.data}},'status': 'success'}
            return JsonResponse(data)
        else:
            data = {'data': wallet_serializer.errors,'status': 'Failed'}
            return JsonResponse(data)


    def get(self, request):
        userid = request.POST.get('user', 1)
        wallet = UserWallet.objects.get(user_id=userid)
        wallet_serializer = WalletSerializer(wallet)
        if not wallet_serializer.instance.status_wallet:
            data = {'data': {'data': {'wallet': wallet_serializer.data}},'status': 'success'}
            return JsonResponse(data)
        else:
            data = {'data': {'data': {'error': 'disabled'}},'status': 'failed'}
            return JsonResponse(data)

class depositBalance(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        transaction_serializer = UserDepositTransactionSerializer(data=request.data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()

            data = {"status": "success","data": {"deposit": transaction_serializer.data}}

            return JsonResponse(data)
        else:

            data = {"status": "failed", "data": {"deposit": transaction_serializer.errors}}

            return JsonResponse(data)

class withdrawBalance(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        transaction_serializer = UserWithdrawTransactionSerializer(data=request.data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()

            data = {"status": "success","data": {"withdraw": transaction_serializer.data}}

            return JsonResponse(data)
        else:

            data = {"status": "failed","data": {"withdraw": transaction_serializer.errors}}

            return JsonResponse(data)
