from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list_bodegas/', views.get_bodegas, name='bodegaList'),
    path('create_bodega/', csrf_exempt(views.create_bodegas), name='bodegaCreate'),
    path('list_bodegas/<int:id>', views.get_bodega_id, name='bodegaId'),
    path('list_bodegas/<int:id>/add_producto', views.add_product_bodega, name='addProductoBodega'),
    path('bodegas/', views.list_bodegas, name='listBodegas'),
    path('cantidad_producto_chiper/<str:id>', views.cant_producto_chiper, name='cantidadProductoChiper')
]
