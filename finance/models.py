from django.db import models
from django.conf import settings
from core.utils import random_int
from account.models import User
from product.models import Factor
# Create your models here.



class Gateway(models.Model):
    title = models.CharField('Gateway Title', max_length=100)
    gateway_request_url = models.CharField('Request Url',max_length=150, null= True, blank=True)
    gateway_verify_url = models.CharField('Verify Url', max_length=150, null= True, blank=True)
    gateway_code = models.CharField('Gateway Code', max_length=12)
    is_enable = models.BooleanField('Is Enable', default=True)
    auth_data = models.TextField('Auth Data', null=True, blank=True)

    class Meta:
        verbose_name = 'Gateway'
        verbose_name_plural = 'Gateways'

    def __str__(self):
        return self.title

class Payment(models.Model):
    invoice_num = models.IntegerField('Invoice Number', unique=True)
    amount = models.PositiveIntegerField('Payment Amount', editable=True)
    gateway = models.ForeignKey(Gateway, related_name='Payments', null=True, on_delete=models.PROTECT, blank=True)
    is_paid = models.BooleanField('Is Paid Status', default=False)
    payment_log = models.TextField('Logs', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    authority = models.CharField('Authority', max_length=64, blank=True)
    time = models.DateTimeField('Time', auto_now=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.invoice_num.hex

    