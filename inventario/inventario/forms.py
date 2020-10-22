from django import forms
from django.forms import DateField

from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'direccionTienda',
            'tendero',
            'tienda',
            'estado',

        ]
        labels = {
            'direccionTienda': 'direccionTienda',
            'tendero':'tendero',
            'tienda':'tienda',
            'estado': 'estado',
        }
