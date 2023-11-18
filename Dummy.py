from builtins import print, range
from faker import Faker
import random

class Mensaje:
    def _init_(self, id_persona_origen, id_persona_destino, fecha, contenido):
        self.id_persona_origen = id_persona_origen
        self.id_persona_destino = id_persona_destino
        self.fecha = fecha
        self.contenido = contenido

    def _str_(self):
        return f"De: {self.id_persona_origen} | Para: {self.id_persona_destino} | Fecha: {self.fecha} | Contenido: {self.contenido}"

class GeneradorMensajes:
    def _init_(self, num_mensajes):
        self.num_mensajes = num_mensajes
        self.fake = Faker()

    def generar_mensaje(self):
        id_persona_origen = random.randint(1, 100)
        id_persona_destino = random.randint(1, 100)
        fecha = self.fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")
        contenido = self.fake.text()
        return Mensaje(id_persona_origen, id_persona_destino, fecha, contenido)

    def generar_mensajes(self):
        mensajes = []
        for _ in range(self.num_mensajes):
            mensaje = self.generar_mensaje()
            mensajes.append(mensaje)
        return mensajes

# Crear una instancia del generador de mensajes
generador = GeneradorMensajes(num_mensajes=5)

# Generar mensajes ficticios
mensajes_generados = generador.generar_mensajes()

# Imprimir los mensajes generados
for mensaje in mensajes_generados:
    print(mensaje)