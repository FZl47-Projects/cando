from django.shortcuts import render, HttpResponse
from django.views.generic import View
from product.models import Category, Product, ShowCase
from instruction.models import Instruction, Article


class Success(View):
    def get(self, request):
        context = {
            'message': request.GET.get('message', None)
        }
        return render(request, 'public/success.html',context)


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
    template_name = 'instruction/instruction.html'

    def get(self, request):
        articles = Article.objects.all()
        instructions = Instruction.objects.all()
        context = {
            'instructions': instructions,
            'articles': articles
        }
        return render(request, self.template_name, context)
