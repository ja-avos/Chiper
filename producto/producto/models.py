from djongo import models


class Producto(models.Model):
    """
    Modelo de producto
    """
    _id = models.ObjectIdField()
    name = models.CharField(max_length=40)
    expiration_date = models.DateField()
    promotion = models.BooleanField()
    discount = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        pass
