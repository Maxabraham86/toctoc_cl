
from django.core.management.base import BaseCommand
from main.models import *

class Command(BaseCommand):
            #tipo=(('u','arrendatario'), ('p','arrendador'))

    def handle (self, *args, **kwargs):
        nombre = Usuario.objects.create( 
            nombre_usuario = 'R.R.',
            nombres ="Roger",
            apellidos ="Rabbit",
            rut="15852258-3",
            direccion="calle tinta, comuna navidad,  region,  Toonlandia",
            telefono_personal='956482152',
            correo_e = 'aaa@bbb.ccc',
            tipo_usuario= 'arrendatiario'
        )




    
    
    
    
    
    
    
