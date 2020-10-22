from django.shortcuts import render
from .logic.logic_bodega import get_all_bodegas, create_a_bodega, get_bodega, get_all_productos, create_producto_bodega,\
    get_all_productos_bodega,get_producto, get_producto_total_bodegas
from .forms import BodegaForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def get_bodegas(request):
    """
    renderizacion de html de todas las bodegas
    :param request:
    :return:
    """
    bodegas_list = get_all_bodegas()
    context = {'bodegas_list': bodegas_list}
    print(context)
    return render(request, 'chiper_Totoro/get_all_bodegas.html', context)


def create_bodegas(request):
    """
    renderizacion del html de crear bodegas
    si el form esta lleno de forma correcta crea una bodega
    :param request:
    :return:
    """
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


def get_bodega_id(request, id):
    """
    renderizacion de html de bodega especifica
    :param request:
    :param id: id bodega
    :return:
    """
    bodega = get_bodega(id)
    productos = get_all_productos_bodega(id)
    productos_bodega = []
    for p in productos:
        product = get_producto(p.producto)[0]
        print(product['id'], product['name'])
        product['cantidad'] = p.cantidad
        productos_bodega.append(product)
    context = {'bodega': bodega, 'productos_bodega':productos_bodega}
    return render(request, 'chiper_Totoro/get_bodega_id.html', context)


def add_product_bodega(request, id):
    """
    renderizacion del html para asociar productos con bodegas
    :param request:
    :param id: producto
    :return:
    """
    productos = get_all_productos()
    bodega = get_bodega(id)
    context = {'productos': productos, 'bodega': bodega}
    if request.method == 'POST':
        productId = request.POST.get('productId')
        cantidad = int(request.POST.get('cantidad'))
        create_producto_bodega(productId, bodega, cantidad)
        messages.add_message(request, messages.SUCCESS, 'Se agregó el producto a la bodega')
        return render(request, 'chiper_Totoro/add_producto_bodega.html', context)

    return render(request, 'chiper_Totoro/add_producto_bodega.html', context)


def list_bodegas(request):
    """
    respuesta en formato json de todas las bodegas
    :param request:
    :return: json bodegas
    """
    bodegas = get_all_bodegas()
    context = list(bodegas.values('id', 'address'))
    return JsonResponse(context, safe=False)


def cant_producto_chiper(request, id):
    """
    respuesta en formato json de cantidad de un producto en todas las bodegas de chiper
    :param request:
    :param id: id producto
    :return:
    """
    cant = get_producto_total_bodegas(id)
    context = [{'cantidad' : cant}]
    return JsonResponse(context, safe=False)
