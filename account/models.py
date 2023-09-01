from django.db import models
from django.http import Http404
from django.shortcuts import reverse
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from product.models import Cart


class CustomBaseUserManager(BaseUserManager):

    def create_user(self, phonenumber, password, email=None, **extra_fields):
        """
        Create and save a normal_user with the given phonenumber and password.
        """
        if not phonenumber:
            raise ValueError("The phonenumber must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phonenumber, password, email=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phonenumber=phonenumber, password=password, role='super_user', email=email,
                                **extra_fields)


class NormalUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='user')


class SuperUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='super_user')


class User(AbstractUser):
    ROLE_USER_OPTIONS = (
        ('user', 'normal_user'),
        ('admin', 'admin'),
        ('super_user', 'super_user'),
    )

    name = models.CharField("name", max_length=150, blank=True, default="بدون نام")
    username = None
    first_name = None
    last_name = None
    email = models.EmailField("email address", null=True, default=None)
    phonenumber = PhoneNumberField(region='IR', unique=True)
    # type users|roles
    role = models.CharField(max_length=20, choices=ROLE_USER_OPTIONS, default='user')

    USERNAME_FIELD = "phonenumber"
    REQUIRED_FIELDS = []

    objects = CustomBaseUserManager()
    normal_user = NormalUserManager()
    super_user = SuperUserManager()

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'{self.role} - {self.phonenumber}'

    @property
    def cart(self):
        return self.get_or_create_cart()

    def get_raw_phonenumber(self):
        p = str(self.phonenumber).replace('+98', '')
        return p

    def get_phonenumber(self):
        return str(self.phonenumber)

    def get_phonenumber_with_prefix(self):
        return self.get_raw_phonenumber().replace('+', '')

    def get_full_name(self):
        fl = f'{self.name}'.strip() or 'بدون نام'
        return fl

    def get_email(self):
        return self.email or '-'

    def get_last_login(self):
        if self.last_login:
            return self.last_login.strftime('%Y-%m-%d %H:%M:%S')
        return '-'

    def get_dashboard_absolute_url(self):
        url = '#'
        if self.role in ('super_user', 'admin'):
            url = reverse('account:dashboard_admin')
        elif self.role in ('user',):
            url = reverse('account:dashboard_user')
        return url

    def get_or_create_cart(self):
        cart = self.cart_set.filter(is_active=True).first()
        if cart is None:
            cart = Cart.objects.create(user=self)
        return cart

    def get_current_cart(self,raise_err=False):
        cart = self.cart_set.filter(is_active=True).first()
        if cart is None and raise_err:
            raise Http404
        return cart

    def get_addresses(self):
        return self.address_set.all()
