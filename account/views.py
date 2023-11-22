from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.utils import form_validate_err, random_int
from core.notify import send_sms
from account.auth.decorators import admin_role_required_cbv, user_role_required_cbv
from product.models import (
    Category, CustomOrderProduct,
    FactorCakeImage, Product,
    ShowCase, Cart,
    Comment
)
from . import forms, models
from config.settings import RESET_PASSWORD_CONFIG
from requests import request
from core.redis import set_value_expire, remove_key, get_value
from django.http import Http404


class Login(View):
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = request.POST
        f = forms.LoginForm(data)
        if form_validate_err(request, f) is False:
            return redirect('account:login')
        username = f.cleaned_data.get('phonenumber')
        password = f.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'کاربری با این مشخصات یافت نشد')
            return redirect('account:login')
        login(request, user)
        messages.success(request, 'خوش امدید')
        try:
            return redirect(data.get('next'))
        except:
            pass
        if user.role in ('super_user',):
            return redirect('account:dashboard_admin')
        return redirect('public:index')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('public:index')


class Register(View):
    template_name = 'account/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = request.POST
        f = forms.RegisterUserFullForm(data)
        if form_validate_err(request, f) is False:
            referer_url = request.META.get('HTTP_REFERER')
            return redirect(referer_url or '/')
            # return render(request, self.template_name)
        data = f.cleaned_data
        user = models.User.objects.create_user(
            name=data.get('name'),
            phonenumber=data.get('phonenumber'),
            password=data.get('password')
        )
        login(request, user)
        code = random_int(size=RESET_PASSWORD_CONFIG['CODE_LENGTH'])
        print(code)
        send_sms('confirmation_code', user.phonenumber, code=code)
        set_value_expire('confirmation_code{user.phonenumber}', code, RESET_PASSWORD_CONFIG['TIMEOUT'])

        try:
            return redirect(request.POST.get('next'))
        except:
            pass
        # return redirect('account:confirmation_code')
        return redirect('public:index')


# confirm phone nmuber for signup
class SignUpConfirmationCode(View):
    template_name = 'account/confirmation.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        post = request.POST
        user = request.user
        entry_code = request.POST.get('confirmation_code')
        code = get_value('confirmation_code{user.phonenumber}')
        if entry_code != code:
            messages.error(request, 'کد وارد شده صحیح نمی باشد')
            return redirect('account:confirmation_code')
        user.is_phonenumber_confirmed = True
        messages.success(request, 'حساب شما با موفقیت ساخته شد')
        send_sms('welcome', user.phonenumber, name=user.name)
        return redirect('public:index')


# get phone number to sned reset password code
class GetPhoneNumber(View):
    template_name = 'account/reset_password.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        phonenumber = request.POST.get('phonenumber', None)
        try:
            user = models.User.objects.get(phonenumber=phonenumber)
        except models.User.DoesNotExist:
            raise Http404("Given phonenumer not found....")
        set_value_expire('{phonenumber}', phonenumber, RESET_PASSWORD_CONFIG['TIMEOUT'])
        code = random_int(size=RESET_PASSWORD_CONFIG['CODE_LENGTH'])
        print(code)
        send_sms('confirmation_code', phonenumber, code=code)
        set_value_expire('confirmation_code{phonenumber}', code, RESET_PASSWORD_CONFIG['TIMEOUT'])
        return redirect('account:reset_password')


# send and check code
class ResetPasswordConfirmationCode(View):
    template_name = 'account/reset_password_confirm.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        phonenumber = get_value('{phonenumber}')
        # print(phonenumber)
        entry_code = request.POST.get('reset_confirmation_code')
        # print(entry_code)
        code = get_value('confirmation_code{phonenumber}')
        if entry_code != code:
            messages.error(request, 'کد وارد شده صحیح نمی باشد')
            return redirect('account:reset_password')
        remove_key('confirmation_code{phonenumber}')
        return redirect('account:change_password')


# change password
class ResetPassword(View):
    template_name = 'account/change_password.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        new_password = request.POST.get('new_password')
        new_password2 = request.POST.get('new_password2')
        if new_password != new_password2:
            messages.error(request, 'رمز های وارد شده یکسان نمی باشند')
            return redirect('account:change_password')
        phonenumber = get_value('{phonenumber}')
        user = models.User.objects.get(phonenumber=phonenumber)
        user.set_password(new_password)
        user.save()
        return redirect('account:login')


# Dashboard admin

class DashboardAdmin(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'products': Product.objects.all(),
            'showcase': ShowCase.objects.first(),
            'showcase_products': Product.objects.filter(category__type_name='showcase'),
            'custom_orders': CustomOrderProduct.objects.filter(is_checked=False),
            'carts_processing': Cart.objects.filter(cartstatus__status='accepted'),
            'carts': Cart.objects.exclude(cartstatus=None),
        }
        return render(request, 'account/dashboard/admin/index.html', context)


class DashboardAdminProducts(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'account/dashboard/admin/products.html', context)


class DashboardAdminCategories(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'account/dashboard/admin/categories.html', context)


class DashboardAdminCustomOrders(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'orders': CustomOrderProduct.objects.filter(is_checked=False)
        }
        return render(request, 'account/dashboard/admin/custom-order-product.html', context)


class DashboardAdminFactorCakeImage(View):

    @admin_role_required_cbv
    def get(self, request):
        factors = FactorCakeImage.objects.all()
        search_content = request.GET.get('search_content')
        if search_content:
            factors = factors.filter(track_code=search_content)
        context = {
            'factors': factors
        }

        return render(request, 'account/dashboard/admin/factor-cake-image.html', context)


class DashboardAdminOrders(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'carts': models.Cart.objects.exclude(factor__factorpayment=None).exclude(cartstatus__status='delivered'),
            'carts_delivered': models.Cart.objects.filter(cartstatus__status='delivered'),
        }
        return render(request, 'account/dashboard/admin/orders.html', context)


class DashboardAdminComments(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'comments': Comment.objects.all(),
            'comments_need_to_check': Comment.objects.filter(is_accepted=False)
        }
        return render(request, 'account/dashboard/admin/comments.html', context)


class DashboardUser(LoginRequiredMixin, View):

    @user_role_required_cbv
    def get(self, request):
        return render(request, 'account/dashboard/user/index.html')


class DashboardUserOrders(LoginRequiredMixin, View):

    @user_role_required_cbv
    def get(self, request):
        return render(request, 'account/dashboard/user/orders.html')


class DashboardUserCustomOrders(LoginRequiredMixin, View):
    # TODO

    def get(self, request):
        context = {
            'orders': request.user.customorderproduct_set.all()
        }
        return render(request, 'account/dashboard/user/custom-orders.html', context)


class DashboardUserProductFavorites(LoginRequiredMixin, View):

    @user_role_required_cbv
    def get(self, request):
        context = {
            'products': request.user.get_or_create_product_favorite_list().products.all()
        }
        return render(request, 'account/dashboard/user/favorites.html', context)


class UsersList(View):
    def get(self, request):
        users = models.User.objects.filter(role='user')
        context = {
            'users': users
        }
        return render(request, 'account/dashboard/admin/list-of-users.html', context)


class AdminList(View):
    def get(self, request):
        users = models.User.objects.filter(role='admin')
        context = {
            'users': users
        }
        return render(request, 'account/dashboard/admin/list-of-users.html', context)
