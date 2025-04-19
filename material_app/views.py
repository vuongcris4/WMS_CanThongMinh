from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, Unit, MaterialUnit, MaterialTransactions
from .forms import MaterialForm, UnitForm, MaterialUnitForm, MaterialTransactionForm
from django.db.models import Sum, Q
from datetime import datetime, timedelta

# Quản lý nguyên vật liệu
"""
Trả về màn hình chính
"""
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

"""
Nếu GET: trả về form nhập
Nếu POST: Save vào form và quay về màn hình list
"""
def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'materials/add_material.html', {'form': form})

"""
Quy đổi đơn vị cho ốc vít
0.0005 kg
0.5 g
1.0 cái

Thêm đơn vị quy đổi cho ốc vít

-> Quản lí các đơn vị cho một loại Material

Nếu POST: trả về list units theo Material
Nếu GET: render Manage_Units, và form nhập
"""
def manage_units(request, material_id):
    material = get_object_or_404(Material, id=material_id)

    # MaterialUnit là bảng chung giữa Material và Units many to many relationship
    units = MaterialUnit.objects.filter(materialId=material).order_by('conversion_factor')
    if request.method == 'POST':
        form = MaterialUnitForm(request.POST)
        if form.is_valid():
            material_unit = form.save(commit=False)
            material_unit.materialId = material
            material_unit.save()
            print(units)
            # Sau khi thêm xong thì trả về Material_Units để load lại full cái bảng
            return render(request, 'materials/partial/material_units.html', {'material_units': units})
    else:
        form = MaterialUnitForm()
    return render(request, 'materials/manage_units.html', {'material': material, 'material_units': units, 'form': form})


# Quản lý đơn vị
"""
Nếu GET: Render add_unit.html, có thêm đơn vị và load danh sách đơn vị
Nếu POST: trả vể cụ unit_list.html để HTMX vào id của page add_unit
"""
def add_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            units = Unit.objects.all()
            return render(request, 'units/unit_list.html', {'units': units})
    else:
        form = UnitForm()
    units = Unit.objects.all()
    return render(request, 'units/add_unit.html', {'form': form, 'units': units})

"""
Load màn hình chính của tồn kho
"""
def inventory(request):
    materials = Material.objects.all()
    return render(request, 'inventory/inventory.html', {'materials': materials})

"""
Khi select đơn vị khác (vd trong tồn kho)
-> Lấy material_id, và lấy unit_id
-> Tìm conversion_factor theo materialId và unitId
-> Lấy inventory_level * conversion_factor
"""
def get_inventory_in_selected_unit_view(request, material_id):
    selected_unit_id = request.GET['unit_id']
    material_unit = MaterialUnit.objects.get(materialId=material_id, unitId=selected_unit_id)
    conversion_factor = material_unit.conversion_factor

    material = Material.objects.get(id=material_id)
    inventory_level = material.inventory_level  # Lấy tồn kho theo base_unitId

    ton_kho = inventory_level * conversion_factor
    return HttpResponse(ton_kho)

"""
Trả về lịch sử transactions
"""
def transaction_history(request, material_id=None):
    if material_id:
        transactions = MaterialTransactions.objects.filter(materialId=material_id).order_by('-created_at')
    else:
        transactions = MaterialTransactions.objects.all().order_by('-created_at')
    return render(request, 'inventory/transaction_history.html', {'transactions': transactions})

"""
Nếu GET: Lấy form thêm Nhập Xuất Tồn
Nếu POST: Post Object đó vào database
"""
def add_transaction(request):
    if request.method == 'POST':
        form = MaterialTransactionForm(request.POST)
        if form.is_valid():
            form.save()  # Khi save, chạy def save base_quantity, sau đó tự kích hoạt signal tính tồn kho
            return redirect('inventory')
    else:
        form = MaterialTransactionForm()
    return render(request, 'inventory/add_transaction.html', {'form': form})

def search_transaction_table(request):
    transaction_type = request.GET.get('transaction_type', '')
    date_range = request.GET.get('flatpickr-date', '')
    search_material = request.GET.get('search_material', '')

    query = Q()
    if transaction_type:
        query &= Q(transaction_type=transaction_type)

    if search_material:
        query &= Q(materialId__name__unaccent__icontains=search_material)

    if date_range:
        try:
            start_date_str, end_date_str = date_range.split(' to ')
            start_date = datetime.strptime(start_date_str, '%d/%m/%y')
            end_date = datetime.strptime(end_date_str, '%d/%m/%y')
        except ValueError:
            start_date = datetime.strptime(date_range, '%d/%m/%y')
            end_date = start_date
        end_date = end_date + timedelta(days=1) - timedelta(seconds=1)
        query &= Q(created_at__range=[start_date, end_date])

    transactions = MaterialTransactions.objects.filter(query).order_by('-created_at')
    context = {'transactions': transactions}
    return render(request, 'inventory/partial/transaction_table.html', context)
