from django import forms
from .models import Tendero, SupervisorBodega


class TenderoForm(forms.ModelForm):
    """
    form con el que se creara un tendero
    """
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



class SupervisorBodegaForm(forms.ModelForm):
    """
    form con el que se creara un supervisor de bodega
    """
    class Meta:
        model = SupervisorBodega
        fields = [
            'name', 'mail', 'password', 'personalId'
        ]
        labels = {
            'name': 'Nombre',
            'mail': 'Correo',
            'password': 'Contraseña',
            'personalId': 'Cédula',
        }
