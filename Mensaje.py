class Mensaje:
    def __init__(self, id_persona_origen, id_persona_destino, fecha, contenido):
        self.id_persona_origen = id_persona_origen
        self.id_persona_destino = id_persona_destino
        self.fecha = fecha
        self.contenido = contenido

    def __str__(self):
        return f"De: {self.id_persona_origen} | Para: {self.id_persona_destino} | Fecha: {self.fecha} | Contenido: {self.contenido}"