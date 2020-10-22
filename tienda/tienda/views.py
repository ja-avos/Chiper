from django.shortcuts import render
from .logic.logic_tienda import get_all_tiendas, create_a_tienda, get_tienda, get_all_productos, create_producto_tienda,\
    get_all_productos_tienda, get_producto, get_all_tenderos, get_tendero_tienda
from .forms import TiendaForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from chiper_Totoro.auth0backend import getRole


@login_required
def get_tiendas(request):
    """
    renderizacion del html de todas las tiendas
    :param request:
    :return:
    """
    role = getRole(request)
    if role['role'] =='Administrador':
        tiendas_list = get_all_tiendas()
        context = {'tiendas_list': tiendas_list}
        print(context)
        return render(request, 'chiper_Totoro/get_all_tiendas.html', context)
    return HttpResponse('Unauthorized user')


def create_tiendas(request):
    """
    renderizacion del html de creacion de tienda
    si el form esta lleno lo verifica y si es correcto se hace post en la db
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            create_a_tienda(form)
            messages.add_message(request, messages.SUCCESS, 'Tienda creada de manera satisfactoria')
            return HttpResponseRedirect(reverse('tiendaList'))
        else:
            print(form.errors)
    else:
        form = TiendaForm()

    context = {
        'form': form,
    }
    return render(request, 'chiper_Totoro/create_tienda.html', context)


def get_tienda_id(request, id):
    """
    renderizacion de html de tienda especifica
    :param request:
    :param id: id de la tienda
    :return:
    """
    role = getRole(request)
    mail = ''
    try:
        tendero = get_tendero_tienda(id)
        mail = tendero[0]['mail']
        if role['role'] == 'Administrador' or (role['role'] == 'Propietario' and role['name'] == mail):
            tienda = get_tienda(id)
            productos = get_all_productos_tienda(id)
            productos_tienda = []
            for p in productos:
                product = get_producto(p.producto)[0]
                product['cantidad'] = p.cantidad
                productos_tienda.append(product)
            context = {'tienda': tienda, 'productos_tienda': productos_tienda}
            return render(request, 'chiper_Totoro/get_tienda_id.html', context)
    except:
        return HttpResponse('Unauthorized access')


def add_product_tienda(request, id):
    """
    renderizacion de html de agregar productos a tienda
    si el form esta completo y correcto se hace post del producto
    :param request:
    :param id:
    :return:
    """
    productos = get_all_productos()
    tienda = get_tienda(id)
    context = {'productos': productos, 'tienda': tienda}
    if request.method == 'POST':
        productId = request.POST.get('productId')
        cantidad = int(request.POST.get('cantidad'))
        create_producto_tienda(productId, tienda, cantidad)
        messages.add_message(request, messages.SUCCESS, 'Se agrego el producto a la tienda')
        return render(request, 'chiper_Totoro/add_producto_tienda.html', context)

    return render(request, 'chiper_Totoro/add_producto_tienda.html', context)


def list_tiendas(request):
    """
    json de todas las tiendas de chiper
    :param request:
    :return:
    """
    tiendas = get_all_tiendas()
    context = list(tiendas.values('id', 'address'))
    return JsonResponse(context,safe=False)




