from django.urls import path
from . import views

urlpatterns = [
    # GET, POST lịch sử nhập xuất
    path('material-transactions/', views.material_transactions),
    path('get-name/', views.get_name_from_id),
]
