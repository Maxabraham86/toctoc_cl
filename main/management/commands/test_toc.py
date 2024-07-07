
from django.core.management.base import BaseCommand
from main.models import *

class Command(BaseCommand):
            #tipo=(('u','arrendatario'), ('p','arrendador'))

    def handle (self, *args, **kwargs):
        # usuario = User.objects.create_user(
        #     username = 'PT',
        #     first_name = 'Peter',
        #     last_name = 'Pan',
        #     password = '1234',
        #     email= 'aaa@bbb.ccc'
        # )
        # UserProfile.objects.create( 
        #     rut="19.123.456-6",
        #     direccion="calle tinta, comuna Toonlandia,  region Talca",
        #     telefono_personal='966618410',
        #     user_type= 'arrendador',
        #     user=usuario,
            
        # )
    #1 ero se hace .create() para generar la variable,
    #2 para pruebas se usa el metodo .get() para obtener la cariable y seguir el codigo de la prueba
    
        comuna1 = Comuna.objects.get(nombre='Comuna1')
        comuna2 = Comuna.objects.get(nombre ='Comuna2')
        comuna3= Comuna.objects.get(nombre ='Comuna3')
        comuna4= Comuna.objects.get(nombre ='Comuna4')
        
        inmueble1= Inmueble.objects.create(
            nombre='Casa de Bety',
            descripcion ='Una de las casas en que vivio Betty Boop',
            M2_construidos= 150,
            M2_totales_terreno=250,
            direccion='calle Black & White',
            comuna =comuna1,
            tipo_vivienda = 'casa',
            precio_mensual= 200000,
            cant_estacionamientos =1,
            cant_habitacion =2,
            cant_banos=2
        )
        inmueble2= Inmueble.objects.create(
            nombre='casa de Pepita',
            descripcion ='casa en que Pepita navajas llamó a la policia',
            M2_construidos= 180,
            M2_totales_terreno=250,
            direccion='calle falsa 123',
            comuna =comuna2,
            tipo_vivienda = 'casa',
            precio_mensual= 250000,
            cant_estacionamientos =2,
            cant_habitacion =3,
            cant_banos=3
        )
        inmueble3= Inmueble.objects.create(
            nombre='Country Side',
            descripcion ='Parcela ubicada en los soleados valles transversales',
            M2_construidos= 500,
            M2_totales_terreno=3500,
            direccion='loma de Aguirre',
            comuna =comuna3,
            tipo_vivienda = 'par',
            precio_mensual= 2000000,
            cant_estacionamientos =10,
            cant_habitacion =12,
            cant_banos=8
        )
        
        inmueble4= Inmueble.objects.create(
            nombre='Bolsos Cerrado',
            descripcion ='Gran casa en hermosa y apasible villa rural',
            M2_construidos= 800,
            M2_totales_terreno=1000,
            direccion='ls Comarca 24',
            comuna =comuna4,
            tipo_vivienda = 'par',
            precio_mensual= 1500000,
            cant_estacionamientos =8,
            cant_habitacion =12,
            cant_banos=5
        )
        
        inmueble5= Inmueble.objects.create(
            nombre='El Poni Pisador',
            descripcion ='Taberna y hostal. Inn',
            M2_construidos= 200,
            M2_totales_terreno=250,
            direccion='Bree 524',
            comuna =comuna4,
            tipo_vivienda = 'casa',
            precio_mensual= 750000,
            cant_estacionamientos =10,
            cant_habitacion =15,
            cant_banos=10
        )
        
        print('Datos de prueba agregados correctamente')




    
    
    
    
    
    
    
