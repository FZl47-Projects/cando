from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.utils import form_validate_err
from core.notify import send_sms
from account.auth.decorators import admin_role_required_cbv, user_role_required_cbv
from product.models import (
    Category, CustomOrderProduct,
    FactorCakeImage, Product,
    ShowCase, Cart,
    Comment
)
from . import forms, models


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
            return render(request, self.template_name)
        data = f.cleaned_data
        user = models.User.objects.create_user(
            name=data.get('name'),
            phonenumber=data.get('phonenumber'),
            password=data.get('password')
        )
        login(request, user)
        messages.success(request, 'حساب شما با موفقیت ساخته شد')
        send_sms('welcome', user.phonenumber, name=user.name)
        try:
            return redirect(data.get('next'))
        except:
            pass
        return redirect('public:index')


# Dashboard admin

class DashboardAdmin(View):

    @admin_role_required_cbv
    def get(self, request):
        context = {
            'products': Product.objects.all(),
            'showcase': ShowCase.objects.first(),
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
        search_content = request.GET.get('search-content')
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