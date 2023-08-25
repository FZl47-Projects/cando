from django.shortcuts import render
from django.views.generic import View
from core.utils import send_sms


class Index(View):

    def get(self, request):
        return render(request,'public/home.html')

