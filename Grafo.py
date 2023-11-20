from Mensaje import Mensaje

# INCLUIR PERSONA QUE MÁS Y MENOS MENSAJES HA MANDADO?
# JACOBO: REGISTRAR QUIEN ES EL NODO CON MÁS CONEXIONES

class Arista:
    def __init__(self, nodo_origen, nodo_destino, peso):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.peso = peso

class Nodo:
    def __init__(self, objeto, grado):
        self.objeto = objeto
        self.grado = grado

# Clase grafo
class Grafo:

    def __init__(self, personas):

        self.nodos = [Nodo(persona, 0) for persona in personas]
        self.max_aristas = []
        # Contiene todos los nodos y sus grados

        self.max_nodo = []
        cantidad_nodos = len(personas)
        self.matriz_adyacencia = [[ 0 for j in range(cantidad_nodos)] for i in range(cantidad_nodos)]

    def añadir_mensaje(self, mensaje):

        persona_origen = mensaje.persona_origen
        persona_destino = mensaje.persona_destino

        nodo_origen = None
        nodo_destino = None
        indice  = 0
        while indice < len(self.nodos) or nodo_origen == None or nodo_destino == None:
            if self.nodos[indice].objeto == persona_origen:
                nodo_origen = indice
            elif self.nodos[indice].objeto == persona_destino:
                nodo_destino = indice
            indice += 1

        self.matriz_adyacencia[nodo_origen][nodo_destino] += 1
        self.matriz_adyacencia[nodo_destino][nodo_origen] += 1

        peso_arista = self.matriz_adyacencia[nodo_destino][nodo_origen]

        if len(self.max_aristas) == 0 or self.max_aristas[0] == peso_arista:
            self.max_aristas.append(Arista(nodo_origen, nodo_destino, peso_arista))
        elif self.max_aristas[0].peso < peso_arista:
            self.max_aristas = [Arista(nodo_origen, nodo_destino, peso_arista)]

        # DETERMINAR SI PERSONA_ORIGEN O PERSONA_DESTINO AHORA SON LOS QUE MÁS CONEXIONES TIENEN

    def añadir_mensajes(self, mensajes):
        for mensaje in mensajes:
            self.añadir_mensaje(mensaje)

    # Imprime datos importantes del grado
    def print_datos(self):
        pass

    # Imprime el grafo como lista de adyacencia
    def print_grafo(self):
        pass
