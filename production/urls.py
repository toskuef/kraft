from django.urls import path
from . import views

app_name = 'production'

urlpatterns = [
    path('orders/', views.OrderList.as_view(), name='production_orders'),

]
