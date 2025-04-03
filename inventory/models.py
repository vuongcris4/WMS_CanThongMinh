from django.db import models
from decimal import Decimal

# Đơn vị tính (ví dụ: kg, lít, cái)
class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Sản phẩm (có đơn vị cơ sở)
class Product(models.Model):
    name = models.CharField(max_length=100)
    base_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='base_unit_products')
    units = models.ManyToManyField(Unit, through='ProductUnit')  # Mối quan hệ many-to-many qua bảng trung gian

    def __str__(self):
        return self.name


# Quan hệ giữa sản phẩm và đơn vị tính (hệ số chuyển đổi)
class ProductUnit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    conversion_factor = models.DecimalField(max_digits=10, decimal_places=2)  # Hệ số chuyển đổi sang đơn vị cơ sở

    class Meta:
        unique_together = ('product', 'unit')

    def __str__(self):
        return f"{self.product.name} - {self.unit.name}"


# Giao dịch nhập/xuất hàng
class InventoryTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('in', 'Nhập hàng'),
        ('out', 'Xuất hàng'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Số lượng theo đơn vị
    base_quantity = models.DecimalField(max_digits=10, decimal_places=2,
                                        editable=False)  # Số lượng quy đổi về đơn vị cơ sở
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Tính số lượng quy đổi về đơn vị cơ sở
        product_unit = ProductUnit.objects.get(product=self.product, unit=self.unit)
        self.base_quantity = self.quantity * product_unit.conversion_factor
        # Kiểm tra tồn kho khi xuất hàng
        if self.transaction_type == 'out':
            current_inventory = get_inventory(self.product)
            if current_inventory < self.base_quantity:
                raise ValueError("Không đủ hàng tồn kho")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity} {self.unit.name}"


# Hàm tính tồn kho
def get_inventory(product):
    total_in = InventoryTransaction.objects.filter(
        product=product, transaction_type='in'
    ).aggregate(total=models.Sum('base_quantity'))['total'] or Decimal(0)
    total_out = InventoryTransaction.objects.filter(
        product=product, transaction_type='out'
    ).aggregate(total=models.Sum('base_quantity'))['total'] or Decimal(0)
    return total_in - total_out