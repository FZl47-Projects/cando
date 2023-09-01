from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from core.models import BaseModel


class Address(BaseModel):
    user = models.ForeignKey('account.User',on_delete=models.CASCADE)
    address = models.TextField()
    plate = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=20)
    receiver_phonenumber = PhoneNumberField(region='IR')
    receiver_name = models.CharField(max_length=100)
    map_address = models.ForeignKey('MapAddress',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user} - {self.address[:30]}..'


class MapAddress(BaseModel):
    # TODO will completed in future
    pass