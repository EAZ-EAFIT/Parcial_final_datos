import random

class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

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

def generar_personas(num_personas):
    personas = []
    for id in range(num_personas):
        persona = Persona(str(id), nombre_aleatorio())
        personas.append(persona)
    return personas