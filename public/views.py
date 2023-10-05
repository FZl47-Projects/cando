from django.shortcuts import render, HttpResponse
from django.views.generic import View
from product.models import Category, Product, ShowCase
from instruction.models import Instruction


class Success(View):
    def get(self, request):
        return HttpResponse('عملیات با موفقیت انجام شد')


class Error(View):
    def get(self, request):
        return HttpResponse('عملیات با خطا مواجه شد')


class Index(View):

    def get(self, request):
        context = {
            'showcase': ShowCase.objects.first(),
            'categories': Category.objects.all(),
            'products': Product.objects.all()[:10]
        }
        return render(request, 'public/home.html', context)

class PublicInstructions(View):
    template_name = 'instruction\instruction.html'
    def get(self, request):
        instructions = Instruction.objects.all()
        context = {
            'instructions':instructions
        }
        return render(request, self.template_name, context)

        