from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    tipo_de_usuario = (
        ('arrendador', 'Arrendador'),
        ('arrendatario', 'Arrendatario'),
    )
    rut = models.CharField(max_length=12, blank=False)
    direccion = models.CharField(max_length=255, blank=False)
    telefono_personal = models.CharField(max_length=20, blank=False)
    user_type = models.CharField(max_length=20, choices=tipo_de_usuario)
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    
    def __str__(self):
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.username
        tipo_usuario = self.user_type
        return f'{nombre} {apellido} | {usuario} | {tipo_usuario}'
    
    
# Create your models here.
# class Usuario(models.Model):
#     tipo=(('u','arrendatario'), ('p','arrendador'))
#     nombre_usuario= models.CharField(max_length=120, default='vacio')
#     nombres = models.CharField(max_length=255)
#     apellidos = models.CharField(max_length=255)
#     rut= models.CharField(max_length=10)
#     direccion= models.CharField(max_length=255)
#     telefono_personal= models.CharField(max_length=20)
#     correo_e = models.EmailField()
#     tipo_usuario= models.CharField(max_length=50, choices=tipo)
    

class Comuna(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    
    def _str__(self):
        return self.nombre


class Inmueble(models.Model):
    inmueble_tipo=(
        ('casa','casa'),
        ('depto','departamento'),
        ('par','parcela')
    )
    nombre = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=255)
    M2_construidos = models.IntegerField()
    M2_totales_terreno = models.IntegerField()
    cant_estacionamientos = models.IntegerField()
    cant_habitacion= models.IntegerField()
    cant_banos=models.IntegerField()
    direccion= models.CharField(max_length=255)
#1er intento
    #comuna= models.CharField(max_length=50)#quiero poner relacion con comunas
#2do intento
    comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)
    tipo_vivienda= models.CharField(max_length=100, choices=inmueble_tipo, default='desconocido')
    precio_mensual= models.IntegerField()
    
    def cantidad_banos(self):
        return sum(bano.cantidad for bano in self.bano_set.all())
    
    def cantidad_habitaciones(self):
        return sum(habitacion.cantidad for habitacion in self.habitacion_set.all())
    
    def cantidad_estacionamientos(self):
        return sum(estacionamiento.cantidad for estacionamiento in self.estacionamiento_set.all())
        
    def __str__(self):
        return self.nombre

class Bano(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.cantidad} bano {self.inmueble.nombre}'

class Habitacion(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.cantidad} habitaciones {self.inmueble.nombre}'

class Estacionamiento(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    cubierto = models.BooleanField(default = False)
    
    def __str__(self):
        return f'{self.cantidad} estacionamientos - {self.inmueble.nombre} - {"Cubierto" if self.cubierto else "no cubierto"}'
    
