from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from core.utils import form_validate_err
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
        return redirect('public:index')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('public:index')


class Register(View):
    template_name = 'account/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        data = request.POST
        f = forms.RegisterUserFullForm(data)
        if form_validate_err(request,f) is False:
            return render(request,self.template_name)
        data = f.cleaned_data
        user = models.User.objects.create_user(
            name=data.get('name'),
            phonenumber=data.get('phonenumber'),
            password=data.get('password')
        )
        login(request,user)
        messages.success(request, 'حساب شما با موفقیت ساخته شد')
        return redirect('public:index')
