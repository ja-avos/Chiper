from django.db import models


class Tienda(models.Model):
    """
    modelo de una tienda
    """
    address = models.CharField(max_length=40)


class ProductoTienda(models.Model):
    """
    Modelo de la asociacion entre producto y tienda
    """
    tienda = models.ForeignKey('Tienda', on_delete=models.CASCADE)
    producto = models.CharField(max_length=1000000, null=False, default=None)
    cantidad = models.IntegerField(null=False)
