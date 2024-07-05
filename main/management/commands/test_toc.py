
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

        comuna1 = Comuna.objects.get(nombre='Comuna1')
        comuna2 = Comuna.objects.get(nombre ='Comuna2')
        comuna3 = Comuna.objects.get(nombre ='Comuna3')
        
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
        
        # Bano.objects.create(inmueble=inmueble1, cantidad =2)
        # Habitacion.objects.create(inmueble=inmueble1, cantidad =2)
        # Estacionamiento.objects.create(inmueble=inmueble1, cantidad=1, cubierto=True)

        # Bano.objects.create(inmueble=inmueble2, cantidad =2)
        # Habitacion.objects.create(inmueble=inmueble2, cantidad =3)
        # Estacionamiento.objects.create(inmueble=inmueble2, cantidad=2, cubierto=True)
        
        # Bano.objects.create(inmueble=inmueble3, cantidad =6)
        # Habitacion.objects.create(inmueble=inmueble3, cantidad =12)
        # Estacionamiento.objects.create(inmueble=inmueble3, cantidad=10, cubierto=True)
        
        
        print('Datos de prueba agregaod correctamente')




    
    
    
    
    
    
    
