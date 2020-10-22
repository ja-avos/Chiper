from django import forms


from .models import Tienda


class TiendaForm(forms.ModelForm):
    """
    Form de creacion de una tiendad
    """
    class Meta:
        model = Tienda
        fields = [
            'address'
        ]
        labels = {
            'address': 'Dirección',
        }
