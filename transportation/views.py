from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from core.utils import form_validate_err
from . import forms


class AddressCreate(LoginRequiredMixin, View):
    template_name = 'transportation/address-create.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        referer_url = request.META.get('HTTP_REFERER')
        data = request.POST.copy()
        # set values
        data['user'] = request.user
        f = forms.AddressCreateForm(data)
        if form_validate_err(request,f) is False:
            return redirect(referer_url or '/error')
        f.save()
        messages.success(request,'ادرس با موفقیت اضافه شد')
        # TODO maybe need to change redirect url
        return redirect('product:cart')
