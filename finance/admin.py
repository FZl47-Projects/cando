from django.contrib import admin
from .models import Gateway, Payment

# Register your models here.

admin.site.register(Gateway)
admin.site.register(Payment)