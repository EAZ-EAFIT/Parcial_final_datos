class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

def nombre_aleatorio():
    return "Pepe"

def generar_personas(num_personas):
    personas = []
    for id in range(num_personas):
        persona = Persona(id, nombre_aleatorio)
        personas.append(persona)
    return personas