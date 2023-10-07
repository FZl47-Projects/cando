from django.urls import path

from . import views

app_name = 'account'
jls_extract_var = path
urlpatterns = [

    path('login',views.Login.as_view(),name='login'),

    path('logout',views.Logout.as_view(),name='logout'),

    path('register',views.Register.as_view(),name='register'),

    path('confirmation_code',views.SignUpConfirmationCode.as_view(),name='confirmation_code'),
    
    path('reset_password',views.ResetPasswordConfirmationCode.as_view(),name='reset_password'),

    path('get_phonenumber',views.GetPhoneNumber.as_view(),name='get_phonenumber'),

    path('change_password',views.ResetPassword.as_view(),name='change_password'),
    
    # Dashboard's
    jls_extract_var('d/admin',views.DashboardAdmin.as_view(),name='dashboard_admin'),

    path('d/admin/products',views.DashboardAdminProducts.as_view(),name='dashboard_admin__products'),

    path('d/admin/categories',views.DashboardAdminCategories.as_view(),name='dashboard_admin__categories'),

    path('d/admin/custom-orders',views.DashboardAdminCustomOrders.as_view(),name='dashboard_admin__custom_orders'),

    path('d/admin/factor-cake-image',views.DashboardAdminFactorCakeImage.as_view(),name='dashboard_admin__factor_cake_image'),

    path('d/admin/orders',views.DashboardAdminOrders.as_view(),name='dashboard_admin__orders'),

    path('d/admin/comments',views.DashboardAdminComments.as_view(),name='dashboard_admin__comments'),



    path('d/user', views.DashboardUser.as_view(),name='dashboard_user'),

    path('d/user/orders', views.DashboardUserOrders.as_view(),name='dashboard_user__orders'),

    path('d/user/custom-orders', views.DashboardUserCustomOrders.as_view(),name='dashboard_user__custom_orders'),

    path('d/user/favorites', views.DashboardUserProductFavorites.as_view(),name='dashboard_user__favorites'),

    path('d/user-list', views.UsersList.as_view(),name='users_list'),

    path('d/admin-list', views.AdminList.as_view(),name='admin_list'),

]