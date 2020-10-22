from ..models import Tienda, ProductoTienda
from django.conf import settings
import requests


def get_all_tiendas():
    """
    Todas las tiendas registradas en chiper
    :return: QuerySet de las tiendas de chiper
    """
    tiendas = Tienda.objects.all()
    print(len(tiendas))
    return tiendas


def create_a_tienda(form):
    """
    creacion de una tienda a partir de un form
    :param form:
    :return:
    """
    tienda = form.save()
    tienda.save()
    return ()


def get_tienda(i):
    """
    Tienda con id particular
    :param i: id de la tienda
    :return: Objeto Tienda
    """
    tienda = Tienda.objects.get(id=i)
    return tienda


def create_producto_tienda(producto, tienda, cantidad):
    """
    Agrega la cantidad de un producto a una tienda
    si ya existe se actualiza la cantidad
    :param producto: id de producto
    :param tienda: objeto tienda
    :param cantidad: cantidad de producto
    :return:
    """

    try:
        posible_producto = get_producto_tienda(producto, tienda)
        posible_producto.cantidad += cantidad
        posible_producto.save()
        return ()
    except:
        producto_tienda = ProductoTienda()
        producto_tienda.tienda = get_tienda(tienda.id)
        producto_tienda.producto = producto
        producto_tienda.cantidad = cantidad
        producto_tienda.save()
        return ()


def get_all_productos():
    """
    Comunicacion con el microservicio de productos para obtener un json
    de todos los productos registrados en chiper
    :return: json de productos
    """
    r = requests.get(settings.PATH_PRODUCTO, headers={"Accept":"application/json"})
    productos = r.json()
    return productos


def get_all_productos_tienda(i):
    """
    Todos los productos asociados a una tienda especifica
    :param i: id de la tienda
    :return: QuerySet de productos asociados a una tienda
    """
    productos = ProductoTienda.objects.all()
    productos_tienda = productos.filter(tienda=i)
    return productos_tienda


def get_producto_tienda(ip, it):
    """
    Obtiene un producto de una tienda
    :param ip: id del producto
    :param it: tienda
    :return: producto en la tienda
    """
    producto_tienda = ProductoTienda.objects.get(tienda=it, producto=ip)
    return producto_tienda


def get_producto(i):
    """
    Comunicacion con microservicio de productos para traer un json con la
    informacion de un producto con id especifico
    :param i: id del producto
    :return:json del producto
    """
    r = requests.get(settings.PATH_PRODUCTO+'/'+str(i),  headers={"Accept":"application/json"})
    producto = r.json()
    return producto


def get_all_tenderos():
    r = requests.get(settings.PATH_TENDEROS, headers={'Accept': 'application/json'})
    tenderos = r.json()
    return tenderos


def get_tendero_tienda(i):
    r = requests.get(settings.PATH_TIENDA_TENDEROS+'/'+str(i), headers={'Accept': 'application/json'})
    tendero = r.json()
    return tendero