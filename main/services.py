from main.models import * 

def crear_usuario():
    pass


def crear_inmueble (nombre, descripcion, M2_construidos, M2_totales_terreno, cant_estacionamientos, cant_habidacion, cant_baños, direccion,comuna):
    pass

def publicar_inmueble(inmueble_id):
    p=Inmueble.objects.get(id=inmueble_id)
    inmueble =Inmueble.objects.all()
    print(propiedad)