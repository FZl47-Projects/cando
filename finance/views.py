from django.shortcuts import render
from django.views.generic import View
from .forms import TestForm
from config.settings import ZARINPAL
from core.gateways import zarinpal
# Create your views here.

class Test(View):
    template_name = 'finance/tset.html'
    form_class = TestForm

    def get(self, request):
        return render(request, template_name, {'form':self.form_class})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            payment_link, authotity = zarinpal.zpal_request_handler(
                settings.ZARINPAL['merchant_id'], form.cleaned_data['amount'], 
                'wallet charge', 'amirshamsi2002@gmail.com', None,
            )
            if payment_link is not None:
                return redirect(payment_link)
        return render(request, self.template_name, {'form': form} )
        