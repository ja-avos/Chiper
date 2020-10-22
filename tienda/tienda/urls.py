from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list_tiendas/', views.get_tiendas, name='tiendaList'),
    path('create_tienda/', csrf_exempt(views.create_tiendas), name='tiendaCreate'),
    path('list_tiendas/<int:id>', views.get_tienda_id, name='tiendaId'),
    path('list_tiendas/<int:id>/add_producto', views.add_product_tienda, name='addProductoTienda'),
    path('tiendas/', views.list_tiendas, name='listarTienda')
]
