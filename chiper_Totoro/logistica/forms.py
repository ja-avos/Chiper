from django import forms
from django.forms import DateField

from .models import Bodega, ProductoChiper


class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = [
            'address'
        ]
        labels = {
            'address': 'Dirección',
        }


class ProductoChiperForm(forms.ModelForm):
    expiration_date = DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = ProductoChiper
        fields = [
            'bodega', 'name', 'expiration_date', 'promotion', 'discount', 'price'
        ]
        labels = {
            'bodega': 'Bodega',
            'name': 'Nombre',
            'address': 'Dirección',
            'expiration_date': 'Fecha de expiración',
            'promotion': '¿Es promoción?',
            'discount': 'Descuento',
            'price': 'Precio',
        }
