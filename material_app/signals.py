from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Material, MaterialUnit, MaterialTransactions
from django.db.models import Sum, Case, When, F, FloatField
from django.db import transaction

# Khi thêm Material mới thì tự thêm MaterialUnit theo Based Unit ID = 1
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

# --- Hàm trợ giúp để tính toán và cập nhật tồn kho ---
# Đặt trong transaction.atomic() để đảm bảo an toàn dữ liệu
# Sử dụng select_for_update() để khóa bản ghi Material, tránh race condition
def _update_material_inventory(material_id):
    """
    Tính toán lại và cập nhật tồn kho cho một vật tư cụ thể.
    Hàm này nên được gọi bên trong một khối transaction.atomic().
    """
    try:
        # Lấy và khóa bản ghi Material để việc tính toán và cập nhật được an toàn
        # Nếu nhiều request cùng cập nhật tồn kho 1 lúc, select_for_update sẽ đợi
        material = Material.objects.select_for_update().get(pk=material_id)

        # Tính toán lại tổng tồn kho từ tất cả các giao dịch của vật tư này
        # Dùng base_quantity đã được tính sẵn khi lưu transaction
        inventory_data = MaterialTransactions.objects.filter(
            materialId_id=material_id
        ).aggregate(
            total_inventory=Sum(
                Case(
                    # Cộng vào nếu là giao dịch nhập
                    When(transaction_type='import', then=F('base_quantity')),
                    # Trừ đi nếu là giao dịch xuất
                    When(transaction_type='export', then=-F('base_quantity')),
                    # Mặc định là 0 (cho các trường hợp khác nếu có)
                    default=0.0,
                    # Chỉ định kiểu dữ liệu kết quả
                    output_field=FloatField()
                )
            )
        )

        # Lấy giá trị tồn kho mới, nếu không có giao dịch nào thì là 0.0
        new_inventory_level = inventory_data['total_inventory'] or 0.0

        # Chỉ thực hiện cập nhật vào DB nếu giá trị tồn kho thực sự thay đổi
        # Giúp tránh ghi vào DB không cần thiết và tránh kích hoạt lại signal (nếu có)
        if material.inventory_level != new_inventory_level:
            material.inventory_level = new_inventory_level
            # Chỉ lưu trường inventory_level để tối ưu
            material.save(update_fields=['inventory_level'])
            print(f"Đã cập nhật tồn kho cho '{material.name}' (ID: {material_id}) thành: {new_inventory_level}") # Log (tùy chọn)
        # else:
            # print(f"Tồn kho cho '{material.name}' (ID: {material_id}) không thay đổi: {new_inventory_level}") # Log (tùy chọn)

    except Material.DoesNotExist:
        # Quan trọng: Xử lý trường hợp Material không còn tồn tại
        print(f"Cảnh báo: Không tìm thấy Material với id {material_id} khi đang cập nhật tồn kho.")
        # Bạn có thể log lỗi này chi tiết hơn nếu cần
        pass # Bỏ qua nếu không tìm thấy material
    except Exception as e:
        # Bắt các lỗi khác có thể xảy ra trong quá trình tính toán/cập nhật
        print(f"Lỗi không xác định khi cập nhật tồn kho cho Material ID {material_id}: {e}")
        # Nên log lỗi này để điều tra
        pass


# --- Signal Handler cho sự kiện SAU KHI lưu MaterialTransactions ---
@receiver(post_save, sender=MaterialTransactions)
def material_transaction_post_save_update_inventory(sender, instance, created, **kwargs):
    """
    Cập nhật tồn kho Material sau khi MaterialTransaction được lưu (tạo mới hoặc cập nhật).
    """
    print(f"Signal post_save chạy cho Transaction ID: {instance.id}, Material ID: {instance.materialId_id}")
    # Đảm bảo việc cập nhật tồn kho diễn ra trong một transaction an toàn
    with transaction.atomic():
        _update_material_inventory(instance.materialId_id) # Gọi hàm trợ giúp


# --- Signal Handler cho sự kiện SAU KHI xóa MaterialTransactions ---
@receiver(post_delete, sender=MaterialTransactions)
def material_transaction_post_delete_update_inventory(sender, instance, **kwargs):
    """
    Cập nhật tồn kho Material sau khi MaterialTransaction bị xóa.
    """
    print(f"Signal post_delete chạy cho Transaction ID: {instance.id}, Material ID: {instance.materialId_id}")
    # Đảm bảo việc cập nhật tồn kho diễn ra trong một transaction an toàn
    with transaction.atomic():
        _update_material_inventory(instance.materialId_id) # Gọi hàm trợ giúp