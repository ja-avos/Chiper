from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """
    Form de producto
    """

    class Meta:
        model = Producto
        fields = [
            'name', 'expiration_date', 'promotion', 'discount', 'price',
        ]
        labels = {
            'name': 'Nombre',
            'expiration_date': 'Fecha de vencimiento',
            'promotion': '¿Tiene promoción?',
            'discount': 'Descuento',
            'price': 'Precio',
        }
