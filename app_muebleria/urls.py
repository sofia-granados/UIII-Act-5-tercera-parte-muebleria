from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para Empleados
    path('empleados/', views.inicio_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/', views.actualizar_empleados, name='actualizar_empleados'),
    path('empleados/actualizar/<int:id_empleado>/', views.realizar_actualizacion_empleados, name='realizar_actualizacion'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleados, name='borrar_empleado'),
    
    # URLs para Sucursal
    path('sucursal/', views.inicio_sucursal, name='ver_sucursal'),
    path('sucursal/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursal/actualizar/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursal/actualizar/<int:id_sucursal>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursal/borrar/<int:id_sucursal>/', views.borrar_sucursal, name='borrar_sucursal'),
    
    # URLs para Producto
    path('producto/', views.inicio_producto, name='ver_producto'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/actualizar/<int:id_producto>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),
]