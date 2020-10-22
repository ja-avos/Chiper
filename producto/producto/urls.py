from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list_productos/', views.get_productos, name='productoList'),
    path('list_productos/<str:id>', views.get_producto_detail, name='productoDetail'),
    path('create_producto/', csrf_exempt(views.create_producto), name='productoCreate'),
    path('productos/', views.list_productos, name='listarProducto'),
    path('productos/<str:id>', views.get_producto_json, name='producto')
]
