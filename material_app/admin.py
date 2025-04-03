from django.contrib import admin
from .models import Unit, Material, MaterialUnit, MaterialTransactions
# Register your models here.

admin.site.register(Unit)
admin.site.register(Material)
admin.site.register(MaterialUnit)
admin.site.register(MaterialTransactions)