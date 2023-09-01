from jsonfield import JSONField
from django.shortcuts import reverse
from django.db import models
from django.conf import settings
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

    def get_price(self):
        return self.price


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

    @property
    def orders_is_available(self) -> bool | str:
        orders = self.get_orders()
        for order in orders:
            if order.product.stock < order.count:
                return order.product.name
        return True

    @property
    def have_orders(self):
        orders = self.get_orders()
        custom_orders = self.get_custom_orders()
        if orders.count() == 0 and custom_orders.count() == 0:
            return False
        return True

    def get_orders(self):
        return self.order_set.all()

    def get_custom_orders(self):
        return self.customorderproduct_set.all()

    def get_total_price(self):
        return self.get_orders_price() + self.get_custom_orders_price()

    def get_total_price_for_payment(self):
        tp_conf = settings.TRANSPORTATION_CONFIG
        """
            calculate discount and transportation price or ..
        """
        cart_total = self.get_total_price()
        fee = tp_conf['fee']
        if cart_total > tp_conf['free_if_price_more_than']:
            fee = 0
        total = cart_total + fee
        return total

    def get_orders_price(self):
        return self.get_orders().aggregate(p=models.Sum(
            models.F('product__price') * models.F('count')
        )
        )['p'] or 0

    def get_custom_orders_price(self):
        return self.get_custom_orders().aggregate(p=models.Sum('price'))['p'] or 0

    def get_dict_detail_orders(self):
        orders = []
        # orders
        [orders.append(order.get_dict_detail()) for order in self.get_orders()]
        # custom orders
        [orders.append(order.get_dict_detail()) for order in self.get_custom_orders()]
        return {
            'orders': orders
        }

    def get_track_code_payment(self):
        try:
            return self.factor.factorpayment.authority
        except:
            return 'چیزی یافت نشد'

    def get_receiver_user_info(self):
        address = self.factor.address
        return f'{address.receiver_phonenumber} - {address.receiver_name}'


class Order(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'#{self.id} order - {self.product} - {self.cart.user}'

    def get_total_price(self):
        return self.product.price * self.count

    def get_dict_detail(self):
        return {
            'product': self.product.name,
            'product_price': self.product.get_price(),
            'product_image': self.product.get_image_url(),
            'product_category': self.product.category.name,
            'count': self.count
        }


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

    def get_image_cover(self):
        return self.get_images().first()

    def get_dict_detail(self):
        return {
            'product': 'سفارش دلخواه',
            'product_price': self.price,
            'product_image': self.get_image_cover(),
            'product_category': 'دسته بندی سفارش دلخواه',
            'count': 1
        }


class Factor(BaseModel):
    DELIVERY_TYPE_OPTIONS = (
        ('online', 'online'),
        ('in-person', 'in-person'),
    )

    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE)
    track_code = models.CharField(default=random_str, max_length=20)
    price = models.PositiveBigIntegerField()
    detail = JSONField()
    note = models.TextField(null=True)
    address = models.ForeignKey('transportation.Address', null=True, on_delete=models.SET_NULL)
    delivery_type = models.CharField(choices=DELIVERY_TYPE_OPTIONS, max_length=10)
    process_to_payment = models.BooleanField(default=False) # True if processing to payment(redirected to bank portal)
    ...

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.track_code

    def get_payment_link(self):
        return reverse('product:factor_payment', args=(self.id,))

    def get_price_rial(self):
        return self.price * 10


class FactorPayment(BaseModel):
    factor = models.OneToOneField('Factor', on_delete=models.CASCADE)
    authority = models.CharField(max_length=50)
    detail = models.TextField(null=True)
    price_paid = models.PositiveBigIntegerField()

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} factor payment'


class Discount(BaseModel):
    code = models.CharField(max_length=30)
    price = models.PositiveBigIntegerField()
    expire_at = models.DateTimeField(null=True)
    cart_price_more = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.code
