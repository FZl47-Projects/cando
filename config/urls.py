
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('public.urls',namespace='public')),
    path('p/',include('product.urls',namespace='product')),
    path('u/',include('account.urls',namespace='account')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# TEMP
# unresolved template files
from django.views.generic import TemplateView

urlpatterns.extend([

    # admin dashboard
    path('package-definition',TemplateView.as_view(template_name='unresolved/admin/Package-definition.html'),name='package_definition'),
    path('tickets-admin',TemplateView.as_view(template_name='unresolved/admin/tickets-admin.html'),name='tickets_admin'),
    path('education',TemplateView.as_view(template_name='unresolved/admin/Education.html'),name='eduaction'),
    path('list-operators',TemplateView.as_view(template_name='unresolved/admin/List-of-operators.html'),name='list_operators'),
    path('list-users',TemplateView.as_view(template_name='unresolved/admin/List-of-users.html'),name='list_users'),
    path('users-comments',TemplateView.as_view(template_name='unresolved/admin/User-comments.html'),name='user_comments'),
    path('admin-settings',TemplateView.as_view(template_name='unresolved/admin/Admin-manual-settings.html'),name='admin_settings'),
    path('list-orders',TemplateView.as_view(template_name='unresolved/admin/List-of-orders.html'),name='list_orders'),
    path('monitoring-operators',TemplateView.as_view(template_name='unresolved/admin/Monitoring-operators.html'),name='monitoring_operators'),
    path('monitoring-financial',TemplateView.as_view(template_name='unresolved/admin/Financial-monitoring.html'),name='monitoring_financial'),

    # public index(home)

    # path('basket-shoping',TemplateView.as_view(template_name='unresolved/index/basket-shoping.html'),name='basket_shoping'),

    path('instruction',TemplateView.as_view(template_name='unresolved/index/instruction.html'),name='instruction'),
    path('custom-box',TemplateView.as_view(template_name='unresolved/index/Custom-box.html'),name='custom_box'),
    path('each-product-page',TemplateView.as_view(template_name='unresolved/index/Each-product-page.html'),name='each_product_page'),
    path('order-tracking',TemplateView.as_view(template_name='unresolved/index/Order-tracking.html'),name='order_tracking'),
    path('wallet',TemplateView.as_view(template_name='unresolved/index/wallet.html'),name='wallet'),
    path('points-to-product',TemplateView.as_view(template_name='unresolved/index/Points-to-product.html'),name='points_to_product'),
    path('notification-page',TemplateView.as_view(template_name='unresolved/index/Notification-page.html'),name='notification_page'),
    path('tickets',TemplateView.as_view(template_name='unresolved/index/tickets.html'),name='tickets'),
    path('profile',TemplateView.as_view(template_name='unresolved/index/profile.html'),name='profile'),


])
