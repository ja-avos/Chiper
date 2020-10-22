from django.db import models


class CEO(models.Model):
    """
    modelo de CEO
    """
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    personalId = models.IntegerField()


class CTO(models.Model):
    """
    modelo de CTO
    """
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    personalId = models.IntegerField()


class COO(models.Model):
    """
    modelo de COO
    """
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    personalId = models.IntegerField()


class SupervisorBodega(models.Model):
    """
    modelo de Supervisor de bodega
    """
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    personalId = models.IntegerField()


class Tendero(models.Model):
    """
    modelo de tendero
    """
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    personalId = models.IntegerField()


class TiendaTendero(models.Model):
    """
    modelo de asociacion de tiendas con tenderos
    """
    tienda = models.IntegerField(null=False, default=None)
    tendero = models.ForeignKey('Tendero', on_delete=models.CASCADE)


class BodegaSupervisor(models.Model):
    """
    modelo de asociacion entre bodega y supervisor
    """
    bodega = models.IntegerField(null=False, default=None)
    supervisor = models.ForeignKey('SupervisorBodega', on_delete=models.CASCADE)
