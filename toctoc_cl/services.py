from main.models import * 

def crear_usuario():
    pass


def crear_propiedad (nombre, descripcion, M2_construidos, M2_totales_terreno, cant_estacionamientos, cant_habidacion, cant_baños, direccion,comuna):
    pass

def publicar_propiedad(propiedad_id):
    p=Inmueble.objects.get(id=propiedad_id)
    propiedad =Inmueble.objects.all()
    print(propiedad)