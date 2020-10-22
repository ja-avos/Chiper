from ..models import Producto
from bson import ObjectId

def get_all_productos():
    """
    obtener todos los productos
    :return:
    """
    productos = Producto.objects.all()
    return productos


def create_a_producto(form):
    """
    crear producto a partir del form
    :param form:
    :return:
    """
    producto = form.save()
    return ()


def get_producto(i):
    """
    obtener producto por id
    :param i:
    :return:
    """
    producto = Producto.objects.filter(_id=ObjectId(i))
    return producto
