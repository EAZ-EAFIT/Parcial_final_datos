class Mensaje:
    def __init__(self, persona_origen, persona_destino, fecha, contenido):
        self.persona_origen = persona_origen
        self.id_origen = persona_origen.id
        self.nombre_origen = persona_origen.nombre

        self.persona_destino = persona_destino
        self.id_destino = persona_destino.id
        self.nombre_destino = persona_destino.nombre

        self.fecha = fecha
        self.contenido = contenido

    def __str__(self):
        # IMPRIMIR COMO YEISON
        return f"De: {self.nombre_origen} id: {self.id_origen} | Para: {self.nombre_destino} id: {self.id_destino} | Fecha: {self.fecha} | Contenido: {self.contenido}"