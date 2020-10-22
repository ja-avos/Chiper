from django.shortcuts import render
from .logic.logicPedido import create_a_pedido, create_producto_pedido, get_all_pedidos,get_all_productos,get_all_productos_pedido, get_pedido, get_producto, get_producto_pedido
from .forms import PedidoForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def get_pedidos(request):
    pedidos_list = get_all_pedidos()
    context = {'pedidos_list': pedidos_list}
    print(context)
    return render(request, 'chiper_Totoro/get_all_pedidos.html', context)


def create_pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = create_a_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'Pedido ha sido  ', pedido.estado)
            return HttpResponseRedirect(reverse('pedidoList'))
        else:
            print(form.errors)
    else:
        form = PedidoForm()

    context = {
        'form': form,
    }
    return render(request, 'chiper_Totoro/create_pedido.html', context)


def get_pedido_id(request, id):
    pedido = get_pedido(id)
    productos = get_all_productos_pedido(id)
    productos_pedido = []
    for p in productos:
        product = get_producto(p.producto)[0]
        product['cantidad'] = p.cantidad
        productos_pedido.append(product)
    context = {'pedido': pedido, 'productos_pedido':productos_pedido}
    return render(request, 'chiper_Totoro/get_pedido_id.html', context)


def add_product_pedido(request, id):
    productos = get_all_productos()
    pedido = get_pedido(id)
    context = {'productos': productos, 'pedido': pedido}
    if request.method == 'POST':
        productId = request.POST.get('productId')
        cantidad = int(request.POST.get('cantidad'))
        create_producto_pedido(productId, pedido, cantidad)
        messages.add_message(request, messages.SUCCESS, 'Se agrego el producto a la pedido ', id)
        return render(request, 'chiper_Totoro/add_producto_pedido.html', context)

    return render(request, 'chiper_Totoro/add_producto_pedido.html', context)


def list_pedidos(request):
    pedidos = get_all_pedidos()
    context = list(pedidos.values('id', 'address'))
    return JsonResponse(context, safe=False)

