from django.urls import path
from . import views

app_name = 'instruction'
urlpatterns = [
    path('', views.Instructions.as_view(),name='instructions'),
]