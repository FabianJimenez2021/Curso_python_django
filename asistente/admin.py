from django.contrib import admin
from .models import Categoría, Producto
# Register your models here.

class CategoríaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')

admin.site.register(Categoría, CategoríaAdmin)
admin.site.register(Producto, ProductoAdmin)