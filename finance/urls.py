from django.urls import path

from . import views

app_name = 'finance'
urlpatterns = [
    path('',views.Test.as_view(),name='test'),
    ]