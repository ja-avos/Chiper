from django.db import models


class Usuario(models.Model):
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    personalId = models.IntegerField()

    def __str__(self):
        pass


class Administrador(Usuario):
    def __str__(self):
        pass


class CEO(Administrador):
    def __str__(self):
        return 'CEO %s %s' % (self.name, self.personalId)


class CTO(Administrador):
    def __str__(self):
        return 'CTO %s %s' % (self.name, self.personalId)


class COO(Administrador):
    def __str__(self):
        return 'COO %s %s' % (self.name, self.personalId)


class Captor(Administrador):
    def __str__(self):
        return 'Captor %s %s' % (self.name, self.personalId)


class Picker(Usuario):
    def __str__(self):
        return 'Picker %s %s' % (self.name, self.personalId)


class Consolidador(Usuario):
    def __str__(self):
        return 'Picker %s %s' % (self.name, self.personalId)


class DeliveryGuy(Usuario):
    def __str__(self):
        return 'DeliveryGuy %s %s' % (self.name, self.personalId)


class SupervisorBodega(Usuario):
    def __str__(self):
        return 'SupervisorBodega %s %s' % (self.name, self.personalId)


class Tendero(Usuario):
    def __str__(self):
        return 'Tendero %s %s' % (self.name, self.personalId)
