from django.db import models


class Bodega(models.Model):
    """
    Modelo de Bodega
    """
    address = models.CharField(max_length=40)


class ProductoBodega(models.Model):
    """
    Modelo de la asociacion de producto bodega
    """
    bodega = models.ForeignKey('Bodega', on_delete=models.CASCADE)
    producto = models.CharField(max_length=1000000, null=False, default=None)
    cantidad = models.IntegerField(null=False)
