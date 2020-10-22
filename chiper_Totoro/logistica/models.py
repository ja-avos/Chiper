from django.db import models


class Bodega(models.Model):
    address = models.CharField(max_length=40)


class Producto(models.Model):
    name = models.CharField(max_length=40)
    expiration_date = models.DateField()
    promotion = models.BooleanField()
    discount = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        pass


class ProductoChiper(Producto):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'ProductoChiper %s %s' % (self.name, self.price)
