from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('custom-order-product',views.CustomOrderProduct.as_view(),name='custom_order_product'),
    path('custom-order-product/<int:order_id>/factor/create',views.CustomOrderProductFactorCreate.as_view(),name='custom_order_factor_create'),

    path('factor-cake-image',views.FactorCakeImage.as_view(),name='factor_cake_image'),
    path('factor-cake-image/submit',views.FactorCakeImageSubmit.as_view(),name='factor_cake_image_submit'),

    path('create',views.ProductCreate.as_view(),name='create'),
    path('update/<int:product_id>',views.ProductUpdate.as_view(),name='update'),
    path('delete/<int:product_id>',views.ProductDelete.as_view(),name='delete'),
    path('category/create',views.CategoryCreate.as_view(),name='category_create'),
    path('category/delete/<int:category_id>',views.CategoryDelete.as_view(),name='category_delete'),
]