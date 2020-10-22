from ..models import CEO, COO
from django.conf import settings
import requests


def create_CEO(form):
    """
    Creacion de CEO
    :param form:
    :return:
    """
    ceo = form.save()
    ceo.save()
    return ()


def create_COO(form):
    """
    Creacion de COO
    :param form:
    :return:
    """
    coo = form.save()
    coo.save()
    return ()


def get_all_tiendas():
    """
    Comunicacion con el microservicio de tiendas para obtener todas las tiendas
    :return: json de las tiendas
    """
    r = requests.get(settings.PATH_TIENDAS, headers={"Accept":"application/json"})
    tiendas = r.json()
    return tiendas


def get_all_bodegas():
    """
    Comunicacion con el microservicio de logistica que tiene todas las bodegas
    :return: json de las bodegas
    """
    r = requests.get(settings.PATH_BODEGAS, headers={"Accept":"application/json"})
    bodegas = r.json()
    return bodegas
