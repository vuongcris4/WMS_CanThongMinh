from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='materials'), name='home'),

    # Quản lý nguyên vật liệu
    path('materials/', views.material_list, name='material_list'),
    path('materials/add/', views.add_material, name='add_material'),
    # path('materials/edit/<int:material_id>/', views.edit_material, name='edit_material'),
    # path('materials/delete/<int:material_id>/', views.delete_material, name='delete_material'),
    path('materials/manage_units/<int:material_id>/', views.manage_units, name='manage_units'),
    path('materials/convert/<int:material_id>/', views.convert_unit, name='convert_unit'),

    # Quản lý đơn vị
    path('units/add/', views.add_unit, name='add_unit'),

    # Nhập xuất tồn
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/change_unit/<int:material_id>/', views.change_unit, name='change_unit'),
    # path('inventory/transactions/', views.transaction_history, name='transaction_history'),
    # path('inventory/transactions/<int:material_id>/', views.transaction_history, name='transaction_history_material'),
    path('inventory/add_transaction/', views.add_transaction, name='add_transaction'),
    path('inventory/get_material_units/<int:material_id>/', views.get_material_units, name='get_units'),
]