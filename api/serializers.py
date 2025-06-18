from rest_framework import serializers
from material_app.models import Material, Unit, MaterialTransactions

# Serializer cho Unit
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        # fields = ['name']  # Chọn các trường muốn hiển thị

class MaterialSerializer(serializers.ModelSerializer):
    base_unitId = UnitSerializer()

    class Meta:
        model = Material
        # fields = '__all__'
        fields = ['id', 'name', 'base_unitId', 'inventory_level']  # Chọn các trường muốn hiển thị

# POST
class MaterialTransactionsCreateSerializer(serializers.ModelSerializer):
    # materialId = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())    # để POST JSON ID ĐƯợc r
    # unitId = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())

    class Meta:
        model = MaterialTransactions
        # fields = '__all__'
        fields = ['id', 'materialId', 'unitId', 'quantity', 'base_quantity', 'transaction_type', 'created_at']
        read_only_fields = ['id', 'base_quantity', 'created_at']
        # fields = ['materialId', 'unitId', 'quantity', 'transaction_type']

# GET
class MaterialTransactionsSerializer(serializers.ModelSerializer):
    materialId = MaterialSerializer()
    unitId = UnitSerializer()

    class Meta:
        model = MaterialTransactions
        # fields = '__all__'
        fields = ['id', 'materialId', 'unitId', 'quantity', 'base_quantity', 'transaction_type', 'created_at']
        read_only_fields = ['id', 'base_quantity', 'created_at']
        # fields = ['materialId', 'unitId', 'quantity', 'transaction_type']
