from django import forms
from .models import Product, Unit, ProductUnit, InventoryTransaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'base_unit']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name']

class ProductUnitForm(forms.ModelForm):
    class Meta:
        model = ProductUnit
        fields = ['product', 'unit', 'conversion_factor']

class InventoryTransactionForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = ['product', 'unit', 'quantity', 'transaction_type']
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Ban đầu, để trống danh sách unit
    #     self.fields['unit'].queryset = Unit.objects.none()
    #
    #     # Nếu đã có product được chọn (khi form được submit)
    #     if 'product' in self.data:
    #         try:
    #             product_id = int(self.data.get('product'))
    #             product = Product.objects.get(id=product_id)
    #             # Lấy base_unit và các unit liên quan từ ProductUnit
    #             base_unit = product.base_unit
    #             related_units = product.units.all()
    #             # Kết hợp base_unit và related_units
    #             # units = Unit.objects.filter(
    #             #     id__in=[base_unit.id] + list(related_units.values_list('id', flat=True))
    #             # ).distinct()
    #             self.fields['unit'].queryset = related_units
    #         except (ValueError, TypeError, Product.DoesNotExist):
    #             pass  # Nếu product không hợp lệ, để trống danh sách unit