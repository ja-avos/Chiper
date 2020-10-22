from django.shortcuts import render
from .logic.logic_tendero import get_all_tenderos, create_a_tendero, get_tendero, create_tienda_tendero, \
    get_tiendas_tendero, get_all_tiendas_tendero, get_tendero_json, tendero_tienda
from .logic.logic_CEO import get_all_tiendas, get_all_bodegas
from .logic.logic_supervisor_bodega import create_supervisor, create_bodega_supervisor, get_all_supervisores, \
    get_supervisor, get_supervisor_bodega, get_all_bodegas_supervisor
from .forms import TenderoForm, SupervisorBodegaForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from chiper_Totoro.auth0backend import getRole
from django.http import JsonResponse
from django.core import serializers


@login_required
def get_tenderos(request):
    """
    renderizacion de html para obtener todos los tenderos
    :param request:
    :return:
    """
    role = getRole(request)
    if role['role'] == 'Administrador':
        tenderos_list = get_all_tenderos()
        context = {'tenderos_list': tenderos_list}
        return render(request, 'chiper_Totoro/get_all_tenderos.html', context)
    else:
        return HttpResponse('Unauthorized user')

def create_tenderos(request):
    """
    renderizacion de html para crear un tendero
    si el form esta lleno y esta correcto crea el tendero
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TenderoForm(request.POST)

        if form.is_valid():
            create_a_tendero(form)
            messages.add_message(request, messages.SUCCESS, 'Tendero creado de manera satisfactoria')
            return HttpResponseRedirect(reverse('tenderoCreate'))
        else:
            print(form.errors)
    else:
        form = TenderoForm()

    context = {
        'form': form,
    }
    return render(request, 'chiper_Totoro/create_tendero.html', context)


@login_required
def get_tendero_detail(request, id):
    """
    renderizacion de html de un tendero especifico
    :param request:
    :param id:
    :return:
    """
    role = getRole(request)

    tendero = get_tendero(id)

    if role['role'] =='Administrador' or (role['role'] == 'Propietario' and role['name'] == tendero.mail):
        tiendas_tendero = get_tiendas_tendero(id)

        context = {'tendero': tendero, 'tiendas_tendero': tiendas_tendero}
        return render(request, 'chiper_Totoro/get_tendero_detail.html', context)
    else:
        return HttpResponse('Unauthorized user')



@login_required
def add_tienda_tendero(request, id):
    """
    renderizacion de form
    :param request:
    :param id:
    :return:
    """
    role = getRole(request)
    tendero = get_tendero(id)
    if role['role'] =='Administrador' or (role['role'] == 'Propietario' and role['name'] == tendero.mail):
        tiendas = get_all_tiendas()

        context = {'tiendas': tiendas, 'tendero': tendero}

        if request.method == 'POST':
            tienda = request.POST.get('tiendaId')
            create_tienda_tendero(tienda, tendero)
            messages.add_message(request, messages.SUCCESS, 'Se asoció tienda con tendero')
            return render(request, 'chiper_Totoro/add_tienda_tendero.html', context)
        return render(request, 'chiper_Totoro/add_tienda_tendero.html', context)
    return HttpResponse('Unauthorized user')

def create_supervisor_bodega(request):
    """
    renderizacion de html para crear un supervisor
    si el form esta lleno y esta correcto crea el supervisor
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = SupervisorBodegaForm(request.POST)
        if form.is_valid():
            create_supervisor(form)
            messages.add_message(request, messages.SUCCESS, 'Supervisor de bodega creado de manera satisfactoria')
            return HttpResponseRedirect(reverse('supervisorCreate'))
        else:
            print(form.errors)
    else:
        form = TenderoForm()

    context = {
        'form': form,
    }
    return render(request, 'chiper_Totoro/create_supervisor_bodega.html', context)


def get_supervisores(request):
    """
    renderizacion de html de supervisores
    :param request:
    :return:
    """
    supervisores_list = get_all_supervisores()
    context = {'supervisores_list': supervisores_list}
    return render(request, 'chiper_Totoro/get_all_supervisores.html', context)


def get_supervisor_detail(request, id):
    """
    renderizacion de html de supervisor particular
    :param request:
    :param id:
    :return:
    """
    supervisor = get_supervisor(id)
    try:
        bodega = get_supervisor_bodega(id)
    except:
        bodega = None
    context = {'supervisor': supervisor, 'bodega_supervisor': bodega}
    return render(request, 'chiper_Totoro/get_supervisor_detail.html', context)


def add_bodega_supervisor(request, id):
    """
    renderizacion de html para asociacion entre un supervisor y una bodega
    :param request:
    :param id:
    :return:
    """
    bodegas = get_all_bodegas()
    supervisor = get_supervisor(id)
    context = {'bodegas': bodegas, 'supervisor': supervisor}
    if request.method == 'POST':
        bodega = request.POST.get('bodegaId')
        try:
            create_bodega_supervisor(bodega, supervisor)
            messages.add_message(request, messages.SUCCESS, 'Supervisor de bodega asociado a bodega correctamente')
        except:
            messages.add_message(request, messages.ERROR, 'El supervisor ya está asociado a una bodega')
        return render(request, 'chiper_Totoro/add_bodega_supervisor.html', context)
    return render(request, 'chiper_Totoro/add_bodega_supervisor.html', context)


def tenderos_json(request):
    tenderos = get_all_tenderos()
    context = list(tenderos.values('id', 'name', 'mail'))
    return JsonResponse(context, safe=False)


def tendero_json(request, id):
    tendero = get_tendero_json(id)
    context = list(tendero.values('id', 'name', 'mail'))
    return JsonResponse(context, safe=False)


def tienda_tendero(request, id):
    tendero = tendero_tienda(id)
    context = list(tendero.values('id', 'name', 'mail'))
    return JsonResponse(context, safe=False)

