from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list_bodegas/', views.get_bodegas, name='bodegaList'),
    path('create_bodega/', csrf_exempt(views.create_bodegas), name='bodegaCreate'),
    path('list_bodegas/<int:id>', views.get_bodega_id, name='bodegaId'),
    path('list_productos_chiper/', views.get_productos_chiper, name='productosChiperList'),
    path('create_producto_chiper/', csrf_exempt(views.create_producto_chiper), name='productoChiperCreate'),
]
