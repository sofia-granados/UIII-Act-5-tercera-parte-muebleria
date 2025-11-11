from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Sucursal, Producto

# Vistas para Empleados
def inicio_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        empleado = Empleado(
            fecha_contratacion=request.POST['fecha_contratacion'],
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            cargo=request.POST['cargo'],
            telefono=request.POST['telefono'],
            sueldo=request.POST['sueldo']
        )
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {'empleados': empleados})

def realizar_actualizacion_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.nombre = request.POST['nombre']
        empleado.edad = request.POST['edad']
        empleado.cargo = request.POST['cargo']
        empleado.telefono = request.POST['telefono']
        empleado.sueldo = request.POST['sueldo']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# Vistas para Sucursal
def inicio_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursal.html', {'sucursales': sucursales})

def agregar_sucursal(request):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        sucursal = Sucursal(
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            num_sucursal=request.POST['num_sucursal'],
            encargado=request.POST['encargado'],
            codigo_postal=request.POST['codigo_postal'],
            ciudad=request.POST['ciudad'],
            id_empleado=empleado
        )
        sucursal.save()
        return redirect('ver_sucursal')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursal/agregar_sucursal.html', {'empleados': empleados})

def actualizar_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursales': sucursales})

def realizar_actualizacion_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        sucursal.telefono = request.POST['telefono']
        sucursal.direccion = request.POST['direccion']
        sucursal.num_sucursal = request.POST['num_sucursal']
        sucursal.encargado = request.POST['encargado']
        sucursal.codigo_postal = request.POST['codigo_postal']
        sucursal.ciudad = request.POST['ciudad']
        sucursal.id_empleado = empleado
        sucursal.save()
        return redirect('ver_sucursal')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal, 'empleados': empleados})

def borrar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursal')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# Vistas para Producto
def inicio_producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        # Crear producto
        producto = Producto(
            nombre=request.POST['nombre'],
            categoria=request.POST['categoria'],
            material=request.POST['material'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            color=request.POST['color']
        )
        producto.save()
        
        # Agregar relaciones ManyToMany con sucursales
        sucursales_ids = request.POST.getlist('sucursales')
        for sucursal_id in sucursales_ids:
            sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
            producto.sucursales.add(sucursal)
        
        return redirect('ver_producto')
    
    sucursales = Sucursal.objects.all()
    return render(request, 'producto/agregar_producto.html', {'sucursales': sucursales})

def actualizar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'productos': productos})

def realizar_actualizacion_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.categoria = request.POST['categoria']
        producto.material = request.POST['material']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.color = request.POST['color']
        producto.save()
        
        # Actualizar relaciones ManyToMany
        producto.sucursales.clear()
        sucursales_ids = request.POST.getlist('sucursales')
        for sucursal_id in sucursales_ids:
            sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
            producto.sucursales.add(sucursal)
        
        return redirect('ver_producto')
    
    sucursales = Sucursal.objects.all()
    producto_sucursales = producto.sucursales.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto, 
        'sucursales': sucursales,
        'producto_sucursales': producto_sucursales
    })

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# Vista de inicio
def inicio(request):
    # Estadísticas para mostrar en el inicio
    total_empleados = Empleado.objects.count()
    total_sucursales = Sucursal.objects.count()
    total_productos = Producto.objects.count()
    
    return render(request, 'inicio.html', {
        'total_empleados': total_empleados,
        'total_sucursales': total_sucursales,
        'total_productos': total_productos
    })