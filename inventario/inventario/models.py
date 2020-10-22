from django.db import models


class Pedido(models.Model):
    direccionTienda = models.CharField(max_length=40)
    tendero = models.IntegerField()
    tienda = models.IntegerField()
    fecha = models.DateField()
    estado = models.CharField(max_length=10)

class ProductoPedido(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    producto = models.IntegerField(null=False, default=None)
    cantidad = models.IntegerField(null=False)
