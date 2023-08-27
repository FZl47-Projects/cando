from django.shortcuts import render
from django.views.generic import View
from product.models import Category, Product


class Index(View):

    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'products': Product.objects.all()[:10]
        }
        return render(request, 'public/home.html', context)
