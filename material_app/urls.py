from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='materials'), name='home'),

    # Hiện trang chủ, danh sách Materials
    path('materials/', views.material_list, name='material_list'),

    # Thêm Material (Load form)
    path('materials/add/', views.add_material, name='add_material'),

    # path('materials/edit/<int:material_id>/', views.edit_material, name='edit_material'),
    # path('materials/delete/<int:material_id>/', views.delete_material, name='delete_material'),

    # Quản lí Units cho từng Material
    path('materials/manage_units/<int:material_id>/', views.manage_units, name='manage_units'),

    # Load danh sách đơn vị và thêm đơn vị
    path('units/add/', views.add_unit, name='add_unit'),

    # Load danh sách ton kho
    path('inventory/', views.inventory, name='inventory'),

    path('get-inventory-in-unit/<int:material_id>/',
         views.get_inventory_in_selected_unit_view,
         name='get_inventory_in_unit'),  # Đặt tên cho URL

    # Lấy lịch sử nhập xuất
    path('inventory/transactions/', views.transaction_history, name='transaction_history'),
    # path('inventory/transactions/<int:material_id>/', views.transaction_history, name='transaction_history_material'),

    # Thêm nhập xuất tồn
    path('inventory/add_transaction/', views.add_transaction, name='add_transaction'),

    path('inventory/search_transaction_table', views.search_transaction_table, name='search_transaction_table'),

]
