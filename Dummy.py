from faker import Faker
import random
import Persona
from Mensaje import Mensaje

class GeneradorMensajes:
    def __init__(self, num_mensajes, num_personas):
        self.num_mensajes = num_mensajes
        self.num_personas = num_personas

    def generar_mensaje(self):
        # EVITAR MENSAJE A SI MISMO
        id_persona_origen = random.randint(1, self.num_personas)
        id_persona_destino = random.randint(1, self.num_personas)

        fecha = Faker().date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")
        contenido = Faker().text()

        return Mensaje(id_persona_origen, id_persona_destino, fecha, contenido)

    def generar_mensajes(self):
        mensajes = []
        for _ in range(self.num_mensajes):
            mensaje = self.generar_mensaje()
            mensajes.append(mensaje)
        return mensajes

def lista_mensajes(num_mensajes, num_personas):
    # Crear una instancia del generador de mensajes
    personas = Persona.generar_personas(num_personas)
    generador = GeneradorMensajes(num_mensajes, num_personas)

    # Generar mensajes ficticios
    mensajes_generados = generador.generar_mensajes()

    return mensajes_generados