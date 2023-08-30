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


class FactorCakeImage(BaseModel, Image):
    user_name = models.CharField(max_length=200)
    track_code = models.CharField(max_length=100)
    description = models.TextField(null=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.user_name


class ShowCase(BaseModel):
    """
        Singleton Model
    """
    products = models.ManyToManyField('Product')

    def __str__(self):
        return 'show case'

    def get_products(self):
        return self.products.all()

    def save(self, *args, **kwargs):
        if ShowCase.objects.count() > 0:
            ShowCase.objects.all().delete()
        super(ShowCase, self).save(*args, **kwargs)


class Cart(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    discount = models.ForeignKey('Discount', null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} cart - {self.user}'

    def get_absolute_url(self):
        # TODO should be completed
        return '#'


class Order(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'#{self.id} order - {self.product} - {self.cart.user}'


class CustomOrderProduct(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    detail = JSONField()
    description = models.TextField(null=True)
    images = models.ManyToManyField('core.Image')
    # complete by admin
    note = models.TextField(null=True)
    is_checked = models.BooleanField(default=False)
    cart = models.ForeignKey('Cart', null=True, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} custom order product'

    def get_images(self):
        return self.images.all()


class Payment(BaseModel):
    # TODO: should be completed
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE)
    track_code = models.CharField(default=random_str, max_length=20)
    price = models.PositiveBigIntegerField()
    price_paid = models.PositiveBigIntegerField(default=0)
    description = models.TextField(null=True)
    address = None
    ...

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.track_code

    def get_payment_link(self):
        # TODO should be completed
        return 'fzlm.ir'


class Discount(BaseModel):
    code = models.CharField(max_length=30)
    price = models.PositiveBigIntegerField()
    expire_at = models.DateTimeField(null=True)
    cart_price_more = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = '-id',
