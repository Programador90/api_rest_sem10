# models.py

from django.db import models

class Producto(models.Model):
    codigoProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=18, decimal_places=2)

class Venta(models.Model):
    codigoVenta = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField()

class DetalleVenta(models.Model):
    codigoVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    codigoProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=18, decimal_places=2)
    descuento = models.DecimalField(max_digits=18, decimal_places=2)
