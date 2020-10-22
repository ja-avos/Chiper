from django.shortcuts import render
from .logic.logic_bodega import get_all_bodegas, get_all_productos_chiper_bodega, create_a_bodega, get_bodega
from .logic.logic_producto_chiper import get_all_productos_chiper, create_a_producto_chiper, get_producto_chiper
from .forms import BodegaForm, ProductoChiperForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from chiper_Totoro.auth0backend import getRole

from ratelimit.decorators import ratelimit


@login_required
@ratelimit(key='ip', rate='5/m')
def get_bodegas(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return HttpResponseRedirect('/')
    role = getRole(request)
    if role == "Administrador":
        bodegas_list = get_all_bodegas()
        context = {'bodegas_list': bodegas_list}
        return render(request, 'chiper_Totoro/get_all_bodegas.html', context)
    else:
        return HttpResponse("Unauthorized User")



@login_required
def create_bodegas(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'POST':
            form = BodegaForm(request.POST)
            if form.is_valid():
                create_a_bodega(form)
                messages.add_message(request, messages.SUCCESS, 'Bodega creada de manera satisfactoria')
                return HttpResponseRedirect(reverse('bodegaList'))
            else:
                print(form.errors)
        else:
            form = BodegaForm()

        context = {
            'form': form,
        }
        return render(request, 'chiper_Totoro/create_bodega.html', context)
    else:
        return HttpResponse("Unauthorized User")


@login_required
def get_bodega_id(request, id):
    role = getRole(request)
    if role == "Administrador":
        bodega = get_bodega(id)
        productos_chiper_bodega = get_all_productos_chiper_bodega(id)
        context = {'bodega': bodega, 'productos_chiper_bodega': productos_chiper_bodega}
        return render(request, 'chiper_Totoro/get_bodega_id.html', context)
    else:
        return HttpResponse("Unauthorized User")


def get_productos_chiper(request):
    productos_chiper_list = get_all_productos_chiper()
    context = {'productos_chiper_list': productos_chiper_list}
    return render(request, 'chiper_Totoro/get_all_productos_chiper.html', context)


def create_producto_chiper(request):
    if request.method == 'POST':
        form = ProductoChiperForm(request.POST)
        if form.is_valid():
            create_a_producto_chiper(form)
            messages.add_message(request, messages.SUCCESS, 'Producto creado de manera satisfactoria')
            return HttpResponseRedirect(reverse('productosChiperList'))
        else:
            print(form.errors)
    else:
        form = ProductoChiperForm()

    context = {
        'form': form,
    }
    return render(request, 'chiper_Totoro/create_producto_chiper.html', context)
