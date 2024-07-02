# Django Imports
from django import forms
from django.core.validators import MinValueValidator

#App Imports
from productos.models import Producto

class RealizarPedido(forms.Form):
    # crea el formulario para realizar el pedido
    producto = forms.ModelChoiceField(
        queryset= Producto.objects.all(),
        widget=forms.Select(
            attrs = {
                'class':'form-control',
                'placeholder': 'Producto',
            }
        )
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {
                'class':'form-control',
                'placeholder': 'ej: 1 servicio',
            }
        ),
        # Validador, el valor minimo que deja cargar es 1.
        validators=[MinValueValidator(1, message= "rambo")]
    )

class DatosInvitado(forms.Form):
    # Formulario que le pide los datos
    #  a los usuarios invitados
    nombre = forms.CharField()
    apellido = forms.CharField()
    teléfono = forms.CharField()