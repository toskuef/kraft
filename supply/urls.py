from django.urls import path
from . import views

app_name = 'supply'

urlpatterns = [
    path('need/', views.NeedView.as_view(), name='supply_purchase'),
    # path('need/is_order/', views.is_order.as_view(), name='supply_purchase_is_order'),
    # path('need/is_not_order/', views.is_not_order.as_view(), name='supply_purchase_is_not_order'),
    path('need/is_booking/', views.is_booking, name='supply_purchase_is_booking'),
    path('need/is_not_booking/', views.is_not_booking, name='supply_purchase_is_not_booking'),
    path('group/', views.group, name='group'),
    path('contractors/', views.ContractorListView.as_view(), name='supply_contractors'),
    path('storage/<int:storage_id>/', views.StorageListView.as_view(), name='supply_storage'),
    path('', views.NomenclatureList.as_view(), name='supply_nomenclature'),

]
