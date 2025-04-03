from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, Unit, MaterialUnit, MaterialTransactions
from .forms import MaterialForm, UnitForm, MaterialUnitForm
from django.db.models import Sum

# Quản lý nguyên vật liệu
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

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

def manage_units(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    units = MaterialUnit.objects.filter(materialId=material).order_by('conversion_factor')
    if request.method == 'POST':
        form = MaterialUnitForm(request.POST)
        if form.is_valid():
            material_unit = form.save(commit=False)
            material_unit.materialId = material
            material_unit.save()
            print(units)
            return render(request, 'materials/partial/material_units.html', {'material_units': units})
    else:
        form = MaterialUnitForm()
    return render(request, 'materials/manage_units.html', {'material': material, 'material_units': units, 'form': form})

def convert_unit(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    units = MaterialUnit.objects.filter(materialId=material)
    if request.method == 'POST':
        quantity = float(request.POST['quantity'])
        from_unit_id = request.POST['from_unit']
        to_unit_id = request.POST['to_unit']
        from_factor = MaterialUnit.objects.get(materialId=material, unitId=from_unit_id).conversion_factor
        to_factor = MaterialUnit.objects.get(materialId=material, unitId=to_unit_id).conversion_factor
        result = (quantity * from_factor) / to_factor
        return render(request, 'materials/convert_result.html', {'result': result, 'to_unit': Unit.objects.get(id=to_unit_id)})
    return render(request, 'materials/convert_form.html', {'material': material, 'units': units})

# Quản lý đơn vị
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

# Nhập xuất tồn
def inventory(request):
    materials = Material.objects.all()
    inventory_data = []
    for material in materials:
        transactions = MaterialTransactions.objects.filter(materialId=material)
        base_quantity = sum(t.base_quantity if t.transaction_type == 'import' else -t.base_quantity for t in transactions)
        units = MaterialUnit.objects.filter(materialId=material)
        inventory_data.append({'material': material, 'base_quantity': base_quantity, 'units': units})
    return render(request, 'inventory/inventory.html', {'inventory_data': inventory_data})

def change_unit(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    unit_id = request.POST['unit']
    transactions = MaterialTransactions.objects.filter(materialId=material)
    base_quantity = sum(t.base_quantity if t.transaction_type == 'import' else -t.base_quantity for t in transactions)
    factor = MaterialUnit.objects.get(materialId=material, unitId=unit_id).conversion_factor
    quantity = base_quantity / factor
    return render(request, 'inventory/quantity.html', {'quantity': quantity})

def transaction_history(request, material_id=None):
    if material_id:
        transactions = MaterialTransactions.objects.filter(materialId=material_id).order_by('-created_at')
    else:
        transactions = MaterialTransactions.objects.all().order_by('-created_at')
    return render(request, 'inventory/transaction_history.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        material_id = request.POST['material']
        unit_id = request.POST['unit']
        quantity = float(request.POST['quantity'])
        transaction_type = request.POST['transaction_type']
        material = Material.objects.get(id=material_id)
        unit = Unit.objects.get(id=unit_id)
        factor = MaterialUnit.objects.get(materialId=material, unitId=unit).conversion_factor
        base_quantity = quantity * factor
        MaterialTransactions.objects.create(
            materialId=material, unitId=unit, quantity=quantity,
            base_quantity=base_quantity, transaction_type=transaction_type
        )
        return redirect('inventory')
    materials = Material.objects.all()
    return render(request, 'inventory/add_transaction.html', {'materials': materials})

def get_units(request, material_id):
    units = MaterialUnit.objects.filter(materialId=material_id)
    return render(request, 'inventory/unit_options.html', {'units': units})