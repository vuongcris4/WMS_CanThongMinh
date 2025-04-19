from django.db import models
from django.core.exceptions import ValidationError

class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)
    base_unitId = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='base_materials')
    units = models.ManyToManyField(Unit, through='MaterialUnit')
    inventory_level = models.FloatField(default=0.0, verbose_name="Tồn kho (ĐV cơ bản)")


    def __str__(self):
        return self.name

# on_delete=models.PROTECT, khi xóa unit nhưng còn object khác liên kết với nó thì không xóa được
class MaterialUnit(models.Model):
    materialId = models.ForeignKey(Material, on_delete=models.CASCADE)
    unitId = models.ForeignKey(Unit, on_delete=models.PROTECT)
    conversion_factor = models.FloatField()

    def __str__(self):
        return f"{self.materialId.name} - {self.unitId.name}"

class MaterialTransactions(models.Model):
    TRANSACTION_TYPES = [
        ('import', 'Nhập'),
        ('export', 'Xuất'),
    ]
    materialId = models.ForeignKey(Material, on_delete=models.CASCADE)
    unitId = models.ForeignKey(Unit, on_delete=models.PROTECT)
    quantity = models.FloatField()
    base_quantity = models.FloatField()  # Số lượng quy đổi về đơn vị cơ bản
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.materialId.name} - {self.quantity} {self.unitId.name}"

    # Tự tính base_quantity khi save MaterialTransactions
    def save(self, *args, **kwargs):
        try:
            # Tìm bản ghi MaterialUnit tương ứng để lấy hệ số quy đổi
            material_unit = MaterialUnit.objects.get(materialId=self.materialId, unitId=self.unitId)
            self.base_quantity = self.quantity / material_unit.conversion_factor
            print("Đã tính base_quantity")
        except MaterialUnit.DoesNotExist:
            raise ValidationError(f"Chưa cấu hình đơn vị '{self.unitId.name}' cho nguyên vật liệu '{self.materialId.name}'.")

        # Gọi phương thức save() gốc của lớp cha để thực hiện lưu vào DB
        super().save(*args, **kwargs)
