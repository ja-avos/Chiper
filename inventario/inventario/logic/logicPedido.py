from django.conf import settings
import requests
from django.http import JsonResponse
from ..models import Pedido
from ..models import ProductoPedido



def get_all_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos


def create_a_pedido(form):
    pedido = form.save()
    pedido.save()
    return pedido


def get_pedido(i):
    pedido = Pedido.objects.get(id=i)
    return pedido


def create_producto_pedido(producto, pedido, cantidad):
    productoGlobal = get_producto(producto)
    try:
        posible_producto = get_producto_pedido(producto, pedido.id)
        
        posible_producto.cantidad += cantidad
        if (posible_producto.cantidad > productoGlobal.cantidad):
            pedido.estado = 'rechazado'
        else:
            pedido.estado = 'aprobado'
        posible_producto.save()
        return ()
    except:
        producto_pedido = ProductoPedido()
        producto_pedido.pedido = get_pedido(pedido.id)
        producto_pedido.producto = producto
        producto_pedido.cantidad = cantidad
        producto_pedido.save()
        return()


def get_all_productos():
    r = requests.get(settings.PATH_PRODUCTO, headers={"Accept":"application/json"})
    productos = r.json()
    return productos


def get_all_productos_pedido(i):
    productos = ProductoPedido.objects.all()
    productos_pedido = productos.filter(pedido=i)
    return productos_pedido


def get_producto_pedido(ip, ib):
    producto_pedido = ProductoPedido.objects.get(producto=ip, pedido=ib)
    return producto_pedido


def get_producto(i):
    r = requests.get(settings.PATH_PRODUCTO+'/'+str(i),  headers={"Accept": "application/json"})
    producto = r.json()
    return producto


def get_tendero(i):
    r = requests.get(settings.PATH_TENDEROS+'/'+str(i), headers={"Accept": "application/json"})
    tendero = r.json()
    return tendero
