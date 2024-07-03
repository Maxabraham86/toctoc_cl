from django.db import models

# Create your models here.
class Usuario(models.Model):
    tipo=(('u','arrendatario'), ('p','arrendador'))
    nombre_usuario= models.CharField(max_length=120, default='vacio')
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    rut= models.CharField(max_length=10)
    direccion= models.CharField(max_length=255)
    telefono_personal= models.CharField(max_length=20)
    correo_e = models.EmailField()
    tipo_usuario= models.CharField(max_length=50, choices=tipo)
    

class Inmueble(models.Model):
    inmueble_tipo=(('c','casa'), ('d','departamento'), ('p','parcela'))
    nombre = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=255)
    M2_construidos = models.IntegerField()
    M2_totales_terreno = models.IntegerField()
    cant_estacionamientos = models.IntegerField()
    cant_habitacion= models.IntegerField()
    cant_baños=models.IntegerField()
    direccion= models.CharField(max_length=255)
    comuna= models.CharField(max_length=50)
    tipo_vivienda= models.CharField(max_length=100, choices=inmueble_tipo, default='desconocido')
    precio_mensual= models.IntegerField()