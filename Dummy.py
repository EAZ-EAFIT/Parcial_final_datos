from faker import Faker
import random
from Mensaje import Mensaje

def generar_mensaje(personas):
    persona_origen = random.choice(personas)
    personas_receptoras = personas[:]
    personas_receptoras.remove(persona_origen)

    persona_destino = random.choice(personas_receptoras)

    fecha = Faker().date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")
    contenido = Faker().text()

    return Mensaje(persona_origen, persona_destino, fecha, contenido)

def generar_mensajes(personas, num_mensajes):
    mensajes = []
    for _ in range(num_mensajes):
        mensaje = generar_mensaje(personas)
        mensajes.append(mensaje)
    return mensajes