from ..models import Bodega, ProductoChiper


def get_all_bodegas():
    bodegas = Bodega.objects.all()
    return bodegas


def get_all_productos_chiper_bodega(i):
    productos_chiper = ProductoChiper.objects.all().filter(bodega=i)
    return productos_chiper


def create_a_bodega(form):
    bodega = form.save()
    bodega.save()
    return ()


def get_bodega(i):
    bodega = Bodega.objects.get(id=i)
    return bodega
