from django.contrib import admin
from .models import Unit, Product, ProductUnit, InventoryTransaction

# Đăng ký các mô hình
admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(ProductUnit)
admin.site.register(InventoryTransaction)