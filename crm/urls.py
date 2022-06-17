from django.urls import path
from . import views
from .services.services import Vkontakte

app_name = 'crm'

urlpatterns = [
    path('addresses/', views.AddressList.as_view(), name='crm_addresses'),
    path('orders/', views.OrderList.as_view(), name='crm_orders'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='crm_order_detail'),
    path('orders/product/<int:pk>/', views.ProductDetail.as_view(), name='crm_product_detail'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view(),
         name='crm_customer_detail'),
    path('customer/<int:pk>/new_task/', views.new_task,
         name='crm_new_task'),
    path('customer/<int:pk>/edit/', views.customer_edit,
         name='crm_customer_edit'),
    path('customer/form_communication/', views.get_form_communication, name='get_form_communication'),
    path('vk/', views.vk),
    path('', views.CustomerList.as_view(), name='crm_customers'),

]

