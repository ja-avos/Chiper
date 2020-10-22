from ..models import Bodega, ProductoBodega
from django.conf import settings
import requests
from django.http import JsonResponse


def get_all_bodegas():
    """
    Todas las bodegas en la base de datos
    :return: QuerySet de todas las bodegas
    """
    bodegas = Bodega.objects.all()
    return bodegas


def create_a_bodega(form):
    """
    Crea modelo Bodega a partir de un form
    :param form:
    :return:
    """
    bodega = form.save()
    bodega.save()
    return ()


def get_bodega(i):
    """
    Bodega con un id particular
    :param i: identificacion de bodega
    :return: bodega
    """
    bodega = Bodega.objects.get(id=i)
    return bodega


def create_producto_bodega(producto, bodega, cantidad):
    """
    Agrega una cantidad de producto a la bodega indicada
    si ya hay de ese producto actualiza la cantidad
    :param producto:
    :param bodega:
    :param cantidad:
    :return:
    """
    try:
        posible_producto = get_producto_bodega(producto, bodega)
        posible_producto.cantidad += cantidad
        posible_producto.save()
        return ()
    except:
        producto_bodega = ProductoBodega()
        producto_bodega.bodega = get_bodega(bodega.id)
        producto_bodega.producto = producto
        producto_bodega.cantidad = cantidad
        producto_bodega.save()
        return ()


def get_all_productos():
    """
    Comunicacion con el microservicio de productos para obtener json de todos los productos
    :return: json de productos
    """
    r = requests.get(settings.PATH_PRODUCTO, headers={"Accept":"application/json"})
    productos = r.json()
    return productos


def get_all_productos_bodega(i):
    """
    Todos los productos de una bodega especifica
    :param i: identificacion de la bodega
    :return: QuerySet de productos en una bodega
    """
    productos = ProductoBodega.objects.all()
    productos_bodega = productos.filter(bodega=i)
    return productos_bodega


def get_producto_bodega(ip, ib):
    """
    Obtiene un producto especifico de una bodega especifica
    :param ip: id producto
    :param ib: id bodega
    :return:
    """
    producto_bodega = ProductoBodega.objects.get(producto=ip, bodega=ib)
    return producto_bodega


def get_producto(i):
    """
    comunicacion con el microservicio de productos para obtener un json del producto con id especifico
    :param i: id producto
    :return:
    """
    r = requests.get(settings.PATH_PRODUCTO+'/'+str(i),  headers={"Accept": "application/json"})
    producto = r.json()
    return producto


def get_producto_total_bodegas(ip):
    """
    Cantidad total de un producto especifico en chiper
    :param ip: id producto
    :return: cantidad de producto
    """
    print(ip)
    bodegas = ProductoBodega.objects.filter(producto=ip)
    print(bodegas)
    total = 0
    for producto in bodegas:
        total += producto.cantidad
    return total
