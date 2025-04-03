from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('units/', views.unit_list, name='unit_list'),
    path('units/create/', views.unit_create, name='unit_create'),
    path('product_units/', views.product_unit_list, name='product_unit_list'),
    path('product_units/create/', views.product_unit_create, name='product_unit_create'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/create/', views.transaction_create, name='transaction_create'),
    path('get_inventory/<str:pk>', views.get_inventory, name='get_inventory'),
    path('get-units/', views.get_units_for_product, name='get-units'),
]