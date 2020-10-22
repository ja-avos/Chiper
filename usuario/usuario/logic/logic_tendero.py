from ..models import Tendero, TiendaTendero


def get_all_tenderos():
    """
    Todos los tenderos que estan asociados a chiper
    :return: QuerySet de todos los tenderos
    """
    tenderos = Tendero.objects.all()
    return tenderos


def create_a_tendero(form, correo):
    """
    crea un tendero por medio de un form llenado en el front
    :param form:
    :return:
    """
    tendero = form.save()
    tendero.save()
    return ()


def create_tienda_tendero(tienda, tendero):
    """
    Asocia una tienda a un tendero
    :param tienda: id de la tienda
    :param tendero: tendero
    :return:
    """
    tienda_tendero = TiendaTendero()
    tienda_tendero.tienda = tienda
    tienda_tendero.tendero = tendero
    tienda_tendero.save()
    return ()


def get_all_tiendas_tendero():
    """
    todas las tiendas que tienen un tendero asociada
    :return: QuerySet de tiendas asociadas a tenderos
    """
    tiendas_tendero = TiendaTendero.objects.all()
    return tiendas_tendero


def get_tiendas_tendero(i):
    """
    Todas las tiendas asociadas a un tendero especifico
    :param i: id del tendero
    :return: QuerySet de la lista de tiendas de un tendero
    """
    tiendas_tendero = TiendaTendero.objects.filter(tendero=i)
    return tiendas_tendero


def get_tendero(i):
    """
    Tendero con id especifico
    :param i: id
    :return: tendero 
    """
    tendero = Tendero.objects.get(id=i)
    return tendero


def get_tendero_json(i):
    tendero = Tendero.objects.filter(id=i)
    return tendero


def get_tendero_email(correo):
    tendero = Tendero.objects.get(mail= correo)
    return tendero


def tendero_tienda(tienda):
    tendero_tienda = TiendaTendero.objects.filter(tienda=tienda)
    tendero = Tendero.objects.filter(id=(tendero_tienda[0].tendero.id))
    return tendero