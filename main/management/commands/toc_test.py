
from django.core.management.base import BaseCommand
from main.models import *

class Command(BaseCommand):
            #tipo=(('u','arrendatario'), ('p','arrendador'))

    def handle (self, *args, **kwargs):
        usuario = User.objects.create_user(
            username = 'RR',
            first_name = 'Roguer',
            last_name = 'Rabit',
            password = '1234',
            email= 'aaa@bbb.ccc'
        )
        UserProfile.objects.create( 
            rut="15852258-3",
            direccion="calle tinta, comuna Toonlandia,  region Talca",
            telefono_personal='956482152',
            user_type= 'arrendatario',
            user=usuario,
            
        )




    
    
    
    
    
    
    
