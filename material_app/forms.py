from django import forms
from .models import Material, Unit, MaterialUnit, MaterialTransactions

class MaterialForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Tên nguyên vật liệu'
        })
    )

    base_unitId = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select select-bordered w-full'
        }),
    )

    class Meta:
        model = Material
        fields = ['name', 'base_unitId']
        labels = {'name': 'Tên nguyên vật liệu', 'base_unitId': 'Đơn vị cơ bản'}

class UnitForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Tên đơn vị'
        })
    )

    class Meta:
        model = Unit
        fields = ['name']
        labels = {'name': 'Tên đơn vị'}

class MaterialUnitForm(forms.ModelForm):
    unitId = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select select-bordered w-full'
        }),
        label='Đơn vị'
    )

    conversion_factor = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Hệ số quy đổi'
        }),
        label='Hệ số quy đổi'
    )

    class Meta:
        model = MaterialUnit
        fields = ['unitId', 'conversion_factor']
        labels = {'unitId': 'Đơn vị', 'conversion_factor': 'Hệ số quy đổi'}

class MaterialTransactionForm(forms.ModelForm):
    materialId = forms.ModelChoiceField(
        queryset=Material.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select select-bordered w-full'
        }),
        label='Nguyên vật liệu'
    )

    unitId = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select select-bordered w-full'
        }),
        label='Đơn vị'
    )

    quantity = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Số lượng'
        }),
        label='Số lượng'
    )

    transaction_type = forms.ChoiceField(
        choices=MaterialTransactions.TRANSACTION_TYPES,
        widget=forms.Select(attrs={
            'class': 'select select-bordered w-full'
        }),
        label='Loại giao dịch'
    )

    class Meta:
        model = MaterialTransactions
        fields = ['materialId', 'unitId', 'quantity', 'transaction_type']
        labels = {
            'materialId': 'Nguyên vật liệu',
            'unitId': 'Đơn vị',
            'quantity': 'Số lượng',
            'transaction_type': 'Loại giao dịch'
        }

        # def __init__(self, *args, **kwargs):
        #     super(MaterialTransactionForm, self).__init__(*args, **kwargs)
        #     # Thêm thuộc tính HTMX cho trường materialId
        #     self.fields['materialId'].widget.attrs.update({
        #         'hx-get': '/inventory/get_material_units/17/',  # URL để gửi yêu cầu
        #         'hx-target': '#unitId',  # Phần tử nhận kết quả
        #         'hx-swap': 'innerHTML',  # Cách thay thế nội dung
        #         'hx-trigger': 'change'  # Sự kiện kích hoạt
        #     })
            # Nếu muốn thêm cho các trường khác, ví dụ unitId:
            # self.fields['unitId'].widget.attrs.update({
            #     'class': 'input'  # Ví dụ thêm class CSS, có thể thêm HTMX nếu cần
            # })

    #
    #
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     # Tính base_quantity dựa trên conversion_factor từ MaterialUnit
    #     material_unit = MaterialUnit.objects.get(materialId=instance.materialId, unitId=instance.unitId)
    #     instance.base_quantity = instance.quantity * material_unit.conversion_factor
    #     if commit:
    #         instance.save()
    #     return instance