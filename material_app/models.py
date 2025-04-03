from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)
    base_unitId = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='base_materials')
    units = models.ManyToManyField(Unit, through='MaterialUnit')

    def __str__(self):
        return self.name

class MaterialUnit(models.Model):
    materialId = models.ForeignKey(Material, on_delete=models.CASCADE)
    unitId = models.ForeignKey(Unit, on_delete=models.CASCADE)
    conversion_factor = models.FloatField()

    def __str__(self):
        return f"{self.materialId.name} - {self.unitId.name}"

class MaterialTransactions(models.Model):
    TRANSACTION_TYPES = [
        ('import', 'Nhập'),
        ('export', 'Xuất'),
    ]
    materialId = models.ForeignKey(Material, on_delete=models.CASCADE)
    unitId = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.FloatField()
    base_quantity = models.FloatField()  # Số lượng quy đổi về đơn vị cơ bản
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.materialId.name} - {self.quantity} {self.unitId.name}"