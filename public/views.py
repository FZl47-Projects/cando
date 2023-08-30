from django.shortcuts import render, HttpResponse
from django.views.generic import View
from product.models import Category, Product


class Success(View):
    def get(self, request):
        return HttpResponse('عملیات با موفقیت انجام شد')


class Error(View):
    def get(self, request):
        return HttpResponse('عملیات با خطا مواجه شد')


class Index(View):

    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'products': Product.objects.all()[:10]
        }
        return render(request, 'public/home.html', context)
