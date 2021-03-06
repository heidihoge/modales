# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=40,blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

class Proveedor(models.Model):
    ruc = models.CharField(unique=True,max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    correo = models.EmailField(null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    fecha = models.DateField(auto_now_add=True)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=5,decimal_places=2)