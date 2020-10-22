from django import forms
from .models import Tendero


class TenderoForm(forms.ModelForm):
    class Meta:
        model = Tendero
        fields = [
            'name', 'mail', 'password', 'personalId'
        ]
        labels = {
            'name': 'Nombre',
            'mail': 'Correo',
            'password': 'Contraseña',
            'personalId': 'Cédula',
        }
