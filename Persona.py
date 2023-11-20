import random

class Persona:
    #La clase persona nos sirve para identificar las personas que creamos con nombre y ID
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

#Función para generar nombres aleatorios
def nombre_aleatorio():
    lista_nombres = [
        "Juan", "María", "José", "Ana", "Pedro", "Isabel", "Luis", "Laura", "Carlos", "Elena",
        "Francisco", "Carmen", "Antonio", "Sofía", "Miguel", "Marta", "Javier", "Beatriz", "Manuel", "Raquel",
        "Fernando", "Lourdes", "Alberto", "Clara", "Esteban", "Jacobo","Diego", "Natalia", "Pablo", "Silvia", "Jorge", "Patricia",
        "Roberto", "Victoria", "Rubén", "Susana", "Alejandro", "Rocío", "David", "Cristina", "Daniel", "Eva",
        "Adrián", "Lucía", "Gonzalo", "Julia", "Sergio", "Beatriz", "Rafael", "Celia", "Arturo", "Lara",
        "Álvaro", "Rosa", "Ignacio", "Carmen", "Lorenzo", "Alicia", "Emilio", "Elisa", "Felix", "Miriam",
        "Víctor", "Angela", "Héctor", "Clara", "José Antonio", "Lidia", "Alfonso", "Paula", "Mario", "Elena",
        "Jaime", "Teresa", "Joaquín", "Mónica", "Gabriel", "Esther", "Guillermo", "Adela", "Raúl", "Marina",
        "Tomás", "Nerea", "Jesús", "Blanca", "Andrés", "Verónica", "Iván", "Aurora", "Ismael", "Nuria"
    ]

    return random.choice(lista_nombres)

#Generamos un numero limitado de objetos de la clase persona  y las guardamos en el arreglo personas[], el cual retornamos
def generar_personas(num_personas):
    personas = []
    for id in range(num_personas):
        persona = Persona(str(id), nombre_aleatorio())
        personas.append(persona)
    return personas