from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list_pedidos/', views.get_pedidos, name='pedidoList'),
    path('create_pedido/', csrf_exempt(views.create_pedidos), name='pedidoCreate'),
    path('list_pedidos/<int:id>', views.get_pedido_id, name='pedidoId'),
    path('list_pedidos/<int:id>/add_producto', views.add_product_pedido, name='addProductoPedido'),
    path('pedidos/', views.list_pedidos, name='listPedidos')
]
