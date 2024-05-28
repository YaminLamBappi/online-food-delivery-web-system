from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer/<int:customer_id>/order/', views.place_order, name='place_order'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('order/success/<int:customer_id>/', views.order_success, name='order_success'),
    
    path('add_subscription/<int:customer_id>/', views.add_subscription, name='add_subscription'),
    path('pay_subscription/<int:customer_id>/<int:plan_id>/', views.pay_subscription, name='pay_subscription'),
   
]