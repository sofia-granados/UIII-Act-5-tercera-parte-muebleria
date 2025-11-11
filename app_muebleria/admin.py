from django.contrib import admin
from .models import Empleado, Sucursal, Producto

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'cargo', 'sueldo', 'fecha_contratacion')
    list_filter = ('cargo',)
    search_fields = ('nombre',)

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id_sucursal', 'num_sucursal', 'ciudad', 'encargado', 'telefono')
    list_filter = ('ciudad',)
    search_fields = ('ciudad', 'encargado')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria', 'material')
    search_fields = ('nombre',)