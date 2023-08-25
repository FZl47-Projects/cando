from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from core.models import Image
from . import models


class CustomOrderProduct(LoginRequiredMixin, View):
    template_name = 'product/custom-order-product.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        images = request.FILES.getlist('image', [])
        image_objects = []
        for image in images:
            if image:
                img_obj = Image.objects.create(image=image)
                image_objects.append(img_obj)

        data = request.POST.copy()

        detail = {
            'taste_spongy': data.get('taste_spongy'),
            'taste_cream': data.get('taste_cream'),
            'filing_cake': data.get('filing_cake'),
            'type_order': data.get('type_order'),
            'date_receive': data.get('date_receive'),
            'hour': data.get('hour'),
            'minute': data.get('minute'),
            'amount_cream': data.get('amount_cream'),
            'weight': data.get('weight'),
            'writing_on_cake': data.get('writing_on_cake'),
            'description': data.get('description'),
        }
        description = data.get('description')
        custom_ord_product_obj = models.CustomOrderProduct.objects.create(
            user=request.user,
            detail=detail,
            description=description
        )
        custom_ord_product_obj.images.add(*image_objects)
        messages.success(request,'سفارش شما با موفقیت ثبت شد')
        return redirect('public:index')