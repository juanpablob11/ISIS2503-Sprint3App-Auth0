from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nombre', 'score_de_confiabilidad', 'cliente']
        labels = {
            'nombre': 'Nombre del Producto',
            'score_de_confiabilidad': 'Score de Confiabilidad',
            'cliente': 'Cliente Asociado',
        }
        help_texts = {
            'score_de_confiabilidad': 'Ingrese un valor entre 0.0 y 1.0.',
        }
        error_messages = {
            'nombre': {
                'max_length': "Este nombre es demasiado largo.",
            },
            'score_de_confiabilidad': {
                'min_value': "El score no puede ser menor que 0.0.",
                'max_value': "El score no puede ser mayor que 1.0.",
            }
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'score_de_confiabilidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }
