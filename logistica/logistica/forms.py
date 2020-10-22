from django import forms
from django.forms import DateField

from .models import Bodega


class BodegaForm(forms.ModelForm):
    """
    Form para la creacion de una bodega
    """
    class Meta:
        model = Bodega
        fields = [
            'address'
        ]
        labels = {
            'address': 'Dirección',
        }
