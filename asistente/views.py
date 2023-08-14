from django.http import HttpResponse, HttpResponseRedirect #JsonResponse
from django.shortcuts import get_object_or_404, render

from asistente.forms import ProductosForm
from .models import Producto

# Create your views here.

# def index (request):
#     productos = Producto.objects.all().values()
#     # return HttpResponse(productos[0].nombre)
#     return JsonResponse(list(productos), safe=False)

#plantillas 
def index (request):
    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context = {'productos' : productos}
        )

def detalle (request, producto_id):
# return HttpResponse(producto_id)
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle.html', context= {'producto' : producto})

def formulario(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductosForm()
    return render(request, 'producto_form.html', {'form' : form})