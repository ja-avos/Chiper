from django.shortcuts import render
from .logic.logic_tendero import get_all_tenderos, create_a_tendero
from .forms import TenderoForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from chiper_Totoro.auth0backend import getRole


@login_required
def get_tenderos(request):
    role = getRole(request)
    if role == "Administrador":
        tenderos_list = get_all_tenderos()
        context = {'tenderos_list': tenderos_list}
        return render(request, 'chiper_Totoro/get_all_tenderos.html', context)
    else:
        return HttpResponse("Unauthorized User")


@login_required
def create_tenderos(request):
    role = getRole(request)
    if role == "Administrador" or role == "Captor":
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
    else:
        return HttpResponse("Unauthorized User")
