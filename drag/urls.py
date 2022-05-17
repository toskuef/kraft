from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('post_2/', views.post_2, name='post_2'),
    path('add/', views.add_drag, name='add_drag'),
    path('del/<int:pk>/', views.del_drag, name='del_drag'),
    path('', views.DragView.as_view(), name='drag'),
]
