from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserWallet(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, editable=True)
    status_wallet = models.BooleanField(default=False)
    disabled_by = models.CharField(max_length=200, null=True)
    disabled_at = models.DateTimeField(editable=False, null=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        self.disabled_at = datetime.datetime.now()
        super(UserWallet, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.name

class UserTransaction(models.Model):
    userwallet = models.ForeignKey(UserWallet, null=False, on_delete=models.CASCADE)
    type_transaction = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(default=0, editable=True)
    reference_id = models.CharField(max_length=100, unique=True)
    deposited_by = models.CharField(max_length=200, null=True)
    deposited_at = models.DateTimeField(editable=False, auto_now_add=True)
    status_transaction = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.deposited_at = datetime.datetime.now()
        super(UserTransaction, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.name