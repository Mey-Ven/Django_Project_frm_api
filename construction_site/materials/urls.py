from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('order/<int:material_id>/', views.order_material, name='order_material'),
    path('orders/', views.order_list, name='order_list'),
]