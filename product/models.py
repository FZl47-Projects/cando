from jsonfield import JSONField
from django.db import models
from core.models import BaseModel, Image
from core.utils import random_str


def upload_src(instance, path):
    frmt = str(path).split('.')[-1]
    return f'product/images/{random_str(20)}.{frmt}'


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    stock = models.PositiveIntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_src, max_length=400)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.name

    def get_image_url(self):
        try:
            return self.image.url
        except:
            # default image
            # TODO: should be completed
            return ''


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_products(self):
        return self.product_set.all()


class CustomOrderProduct(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    detail = JSONField()
    description = models.TextField(null=True)
    images = models.ManyToManyField('core.Image')
    # complete by admin
    note = models.TextField(null=True)
    is_checked = models.BooleanField(default=False)
    factor = models.OneToOneField('Factor', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} custom order product'

    def get_images(self):
        return self.images.all()


class Factor(BaseModel):
    # TODO: should be completed
    track_code = models.CharField(default=random_str, max_length=20)
    price = models.PositiveBigIntegerField()
    price_paid = models.PositiveBigIntegerField(default=0)
    address = None
    ...

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.track_code

    def get_payment_link(self):
        # TODO should be completed
        return 'fzlm.ir'


class FactorCakeImage(BaseModel, Image):
    user_name = models.CharField(max_length=200)
    track_code = models.CharField(max_length=100)
    description = models.TextField(null=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.user_name
