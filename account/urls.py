from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('register',views.Register.as_view(),name='register'),
    # Dashboard's
    path('d/admin',views.DashboardAdmin.as_view(),name='dashboard_admin'),
    path('d/admin/products',views.DashboardAdminProducts.as_view(),name='dashboard_admin__products'),
]