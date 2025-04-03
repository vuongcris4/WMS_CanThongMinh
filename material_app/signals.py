from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Material, MaterialUnit

@receiver(post_save, sender=Material)
def create_base_material_unit(sender, instance, created, **kwargs):
    print("CHECKKKKKK")

    if created:
        # Kiểm tra xem bản ghi với unit là base_unitId đã tồn tại chưa
        if not MaterialUnit.objects.filter(materialId=instance, unitId=instance.base_unitId).exists():

            MaterialUnit.objects.create(
                materialId=instance,
                unitId=instance.base_unitId,
                conversion_factor=1
            )