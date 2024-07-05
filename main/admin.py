from django.contrib import admin
from main.models import Inmueble, Comuna, Bano, Habitacion , Estacionamiento
# Register your models here.


class InmuebleAdmin(admin.ModelAdmin):
    list_display=('nombre', 'tipo_vivienda', 'precio_mensual', 'comuna')
    search_fields= ('nombre', 'direccion')
    list_filter=('tipo_vivienda', 'comuna')
    fieldsets = (
        ('Informacion General',{
            'fields':('nombre', 'descripcion', 'direccion','comuna')
        }),
        ('Dimenciones', {
            'fields':('M2_construidos', 'M2_totales_terreno')
        }),
        ('Detalles', {
            'fields':('tipo_vivienda', 'precio_mensual')
        }),
    )

class BanoAdmin(admin.ModelAdmin):
    list_display=('cantidad', 'inmueble')
    search_fields=['inmueble_nombre']
    
class HabitacionAdmin(admin.ModelAdmin):
    list_display=('cantidad' , 'inmueble')
    search_fields = ['inmueble_nombre']
    
class EstacionamientoAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'cubierto', 'inmueble')
    search_fields= ['inmueble_nombre']
    list_filter=['cubierto']
    

admin.site.register(Inmueble,InmuebleAdmin)
admin.site.register(Comuna)
admin.site.register(Bano, BanoAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Estacionamiento, EstacionamientoAdmin)
