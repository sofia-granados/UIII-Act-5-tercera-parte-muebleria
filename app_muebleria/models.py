from django.db import models

# Choices para los campos
CARGO_CHOICES = [
    ('VENDEDOR', 'Vendedor'),
    ('GERENTE', 'Gerente'),
    ('ALMACEN', 'Almacen'),
    ('CAJERO', 'Cajero'),
]

CATEGORIA_CHOICES = [
    ('SALA', 'Sala'),
    ('COMEDOR', 'Comedor'),
    ('RECAMARA', 'Recámara'),
    ('OFICINA', 'Oficina'),
]

MATERIAL_CHOICES = [
    ('MADERA', 'Madera'),
    ('METAL', 'Metal'),
    ('PLASTICO', 'Plástico'),
    ('VIDRIO', 'Vidrio'),
]

class Empleado(models.Model):
    fecha_contratacion = models.DateField()
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    telefono = models.CharField(max_length=15)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} - {self.cargo}"

class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    num_sucursal = models.IntegerField()
    encargado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=50)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="sucursales")
    
    def __str__(self):
        return f"Sucursal {self.num_sucursal} - {self.ciudad}"

class Producto(models.Model):    
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    precio = models.FloatField()
    stock = models.IntegerField()
    color = models.CharField(max_length=30)
    id_producto = models.AutoField(primary_key=True)
    sucursales = models.ManyToManyField(Sucursal, related_name="productos")
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"