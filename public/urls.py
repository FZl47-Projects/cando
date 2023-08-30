from django.urls import path
from . import views

app_name = 'public'
urlpatterns = [
    path('error', views.Error.as_view(), name='error'),
    path('success', views.Success.as_view(), name='success'),

    path('', views.Index.as_view(), name='index')
]
