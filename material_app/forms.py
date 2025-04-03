from django import forms
from .models import Material, Unit, MaterialUnit

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'base_unitId']
        labels = {'name': 'Tên nguyên vật liệu', 'base_unitId': 'Đơn vị cơ bản'}

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name']
        labels = {'name': 'Tên đơn vị'}

class MaterialUnitForm(forms.ModelForm):
    class Meta:
        model = MaterialUnit
        fields = ['unitId', 'conversion_factor']
        labels = {'unitId': 'Đơn vị', 'conversion_factor': 'Hệ số quy đổi'}