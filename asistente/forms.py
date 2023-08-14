from . import models 
from django.forms import ModelForm

class ProductosForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoría']