
from django.core.management.base import BaseCommand
from main.models import *

class Command(BaseCommand):
            #tipo=(('u','arrendatario'), ('p','arrendador'))

    def handle (self, *args, **kwargs):
        usuario = User.objects.create_user(
            username = 'PT',
            first_name = 'Peter',
            last_name = 'Pan',
            password = '1234',
            email= 'aaa@bbb.ccc'
        )
        UserProfile.objects.create( 
            rut="19.123.456-6",
            direccion="calle tinta, comuna Toonlandia,  region Talca",
            telefono_personal='966618410',
            user_type= 'arrendador',
            user=usuario,
            
        )




    
    
    
    
    
    
    
