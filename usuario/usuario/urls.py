from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list_tenderos/', views.get_tenderos, name='tenderoList'),
    path('create_tendero/', csrf_exempt(views.create_tenderos), name='tenderoCreate'),
    path('list_tenderos/<int:id>', views.get_tendero_detail, name='tenderoDetail'),
    path('list_tenderos/<int:id>/agregar_tienda', views.add_tienda_tendero, name='agregarTiendaTendero'),
    path('create_supervisor_bodega/', csrf_exempt(views.create_supervisor_bodega), name='supervisorCreate'),
    path('list_supervisores/', views.get_supervisores, name='supervisoresList'),
    path('list_supervisores/<int:id>', views.get_supervisor_detail, name='supervisorDetail'),
    path('list_supervisores/<int:id>/agregar_bodega', views.add_bodega_supervisor, name='agregarBodegaSupervisor'),
    path('tenderos/', views.tenderos_json, name='jsonTenderos'),
    path('tenderos/<int:id>', views.tendero_json, name='detailTenderoJson'),
    path('tendero_tienda/<int:id>', views.tienda_tendero, name='duenosTienda')
]
