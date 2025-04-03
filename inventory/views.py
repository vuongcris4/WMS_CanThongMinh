from django.shortcuts import render, redirect
from .models import Product, Unit, ProductUnit, InventoryTransaction
from .forms import ProductForm, UnitForm, ProductUnitForm, InventoryTransactionForm
from django.db import models
from decimal import Decimal
from django.http import HttpResponse, JsonResponse

# Danh sách sản phẩm
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# Thêm sản phẩm
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

# Danh sách đơn vị
def unit_list(request):
    units = Unit.objects.all()
    return render(request, 'inventory/unit_list.html', {'units': units})

# Thêm đơn vị
def unit_create(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = UnitForm()
    return render(request, 'inventory/unit_form.html', {'form': form})

# Danh sách đơn vị của sản phẩm
def product_unit_list(request):
    product_units = ProductUnit.objects.all()
    return render(request, 'inventory/product_unit_list.html', {'product_units': product_units})

# Thêm đơn vị cho sản phẩm
def product_unit_create(request):
    if request.method == 'POST':
        form = ProductUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_unit_list')
    else:
        form = ProductUnitForm()
    return render(request, 'inventory/product_unit_form.html', {'form': form})

# Danh sách giao dịch
def transaction_list(request):
    transactions = InventoryTransaction.objects.all()
    return render(request, 'inventory/transaction_list.html', {'transactions': transactions})

# Thêm giao dịch
def transaction_create(request):
    if request.method == 'POST':
        form = InventoryTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = InventoryTransactionForm()
    return render(request, 'inventory/transaction_form.html', {'form': form})

def get_inventory(request, pk):
    product = Product.objects.get(id=pk)
    total_in = InventoryTransaction.objects.filter(
        product=product, transaction_type='in'
    ).aggregate(total=models.Sum('base_quantity'))['total'] or Decimal(0)
    total_out = InventoryTransaction.objects.filter(
        product=product, transaction_type='out'
    ).aggregate(total=models.Sum('base_quantity'))['total'] or Decimal(0)
    html =f"<html><body><h1>{total_in - total_out}</h1></body></html>"
    return HttpResponse(html)

# View phụ để lấy danh sách unit theo product
def get_units_for_product(request):
    product_id = request.GET.get('product_id')
    if product_id:
        try:
            product = Product.objects.get(id=product_id)
            units = product.units.all()  # Lấy các unit liên quan qua ProductUnit
            unit_options = ''.join([f'<option value="{unit.id}">{unit.name}</option>' for unit in units])
            return HttpResponse(unit_options)
        except Product.DoesNotExist:
            pass
    return HttpResponse('')