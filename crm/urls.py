from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('addresses/', views.AddressList.as_view(), name='crm_addresses'),
    path('orders/', views.OrderList.as_view(), name='crm_orders'),
    path('customer/<int:pk>', views.CustomerDetail.as_view(),
         name='crm_customer_detail'),
    path('', views.CustomerList.as_view(), name='crm_customers'),

]
