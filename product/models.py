from jsonfield import JSONField
from django.db import models
from core.models import BaseModel
from core.utils import random_str


def upload_src(instance, path):
    frmt = str(path).split('.')[-1]
    return f'product/images/{random_str(20)}.{frmt}'


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    stock = models.PositiveIntegerField(default=1)
    categories = models.ManyToManyField('Category')
    image = models.ImageField(upload_to=upload_src)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomOrderProduct(BaseModel):
    user = models.ForeignKey('account.User',on_delete=models.CASCADE)
    detail = JSONField()
    description = models.TextField(null=True)
    images = models.ManyToManyField('core.Image')
    is_paid = models.BooleanField(default=False)
    # complete by admin
    price = models.BigIntegerField(null=True)
    note = models.TextField(null=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} custom order product'
