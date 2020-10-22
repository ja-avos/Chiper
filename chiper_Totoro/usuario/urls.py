from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('list/', views.get_tenderos, name='tenderoList'),
    path('create/', csrf_exempt(views.create_tenderos), name='tenderoCreate'),
]
