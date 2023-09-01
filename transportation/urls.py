from django.urls import path
from . import views

app_name = 'transportation'
urlpatterns = [
    path('address/create',views.AddressCreate.as_view(),name='address_create')
]