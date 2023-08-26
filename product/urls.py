from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('custom-order-product',views.CustomOrderProduct.as_view(),name='custom_order_product'),
    path('create',views.ProductCreate.as_view(),name='create'),
    path('delete/<int:product_id>',views.ProductDelete.as_view(),name='delete'),
]