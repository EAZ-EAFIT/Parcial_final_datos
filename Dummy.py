from faker import Faker
import random
from Mensaje import Mensaje

#Del arreglo personas se elige una al azar como origen, luego se elige una persona destino de un arreglo que no tiene a la persona origen
def generar_mensaje(personas):
    persona_origen = random.choice(personas)
    personas_receptoras = personas[:]
    personas_receptoras.remove(persona_origen)
    persona_destino = random.choice(personas_receptoras)

    #Con faker hacemos los mensajes con fecha y contenido
    fecha = Faker().date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")
    contenido = Faker().text()

    #Retornamos un objeto de la clase mensaje
    return Mensaje(persona_origen, persona_destino, fecha, contenido)

#Generamos un numero limitado de mensajes mediante la funcion generar mensaje y los guardamos en el arreglo mensajes[], el cual retornamos
def generar_mensajes(personas, num_mensajes):
    mensajes = []
    for _ in range(num_mensajes):
        mensaje = generar_mensaje(personas)
        mensajes.append(mensaje)
    return mensajes