from ..models import ProductoChiper


def get_all_productos_chiper():
    productos_chiper = ProductoChiper.objects.all()
    return productos_chiper


def create_a_producto_chiper(form):
    productos_chiper = form.save()
    productos_chiper.save()
    return ()


def get_producto_chiper(i):
    producto_chiper = ProductoChiper.objects.get(id=i)
    return producto_chiper
