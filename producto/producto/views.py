from django.shortcuts import render
from .logic.logic_producto import get_all_productos, create_a_producto, get_producto
from .forms import ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse


def get_productos(request):
    """
    renderizacion de html de todos los productos
    :param request:
    :return:
    """
    productos = get_all_productos()
    prodlist = list(productos.values('_id', 'name', 'expiration_date', 'promotion', 'discount', 'price'))
    for i in prodlist:
        i["id"] = str(i["_id"])
        del i["_id"]
    context = {"productos_list": prodlist}
    return render(request, 'chiper_Totoro/get_all_productos.html', context)


def create_producto(request):
    """
    renderizacion de creacion de producto html de producto
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_a_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto creado de manera satisfactoria')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }
    return render(request, 'chiper_Totoro/create_producto.html', context)


def list_productos(request):
    """
    json de todos los productos
    :param request:
    :return:
    """
    productos = get_all_productos()
    context = list(productos.values('_id', 'name', 'expiration_date', 'promotion', 'discount', 'price'))
    for i in context:
        i["id"] = str(i["_id"])
        del i["_id"]
    return JsonResponse(context, safe=False)


def get_producto_json(request, id):
    """
    producto json por id
    :param request:
    :param id:
    :return:
    """
    producto = get_producto(id)
    context = list(producto.values('_id', 'name', 'expiration_date', 'promotion', 'discount', 'price'))
    for i in context:
        i["id"] = str(i["_id"])
        del i['_id']
    return JsonResponse(context, safe=False)


def get_producto_detail(request, id):
    """
    renderizacion de html de producto particular
    :param request:
    :param id:
    :return:
    """
    producto = get_producto(id)
    prodlist = list(producto.values('_id', 'name', 'expiration_date', 'promotion', 'discount', 'price'))
    for i in prodlist:
        i["id"] = str(i["_id"])
        del i["_id"]
    context = {"producto": prodlist[0]}
    return render(request, 'chiper_Totoro/get_producto_detail.html', context)
