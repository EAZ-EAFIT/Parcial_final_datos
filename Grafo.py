from Mensaje import Mensaje

# INCLUIR PERSONA QUE MÁS Y MENOS MENSAJES HA MANDADO?
# JACOBO: REGISTRAR QUIEN ES EL NODO CON MÁS CONEXIONES

class Arista:
    def __init__(self, nodo_origen, nodo_destino, peso):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.peso = peso

# Clase grafo
class Grafo:

    def __init__(self, personas):

        # self.nodos = []
        self.max_aristas = []
        # Contiene todos los nodos y sus grados

        self.max_nodo = []
        cantidad_nodos = len(personas)

        self.nodo_fila = {}
        self.matriz_adyacencia = []

        for i in range(cantidad_nodos):
            self.matriz_adyacencia.append([])
            for j in range(cantidad_nodos):
                self.matriz_adyacencia[i].append(0)
                self.matriz_adyacencia[i][j] = 0
            self.nodo_fila[i] = personas[i]
            self.nodo_fila[personas[i]] = i

    def añadir_mensaje(self, mensaje):

        persona_origen = str(mensaje.id_persona_origen)
        persona_destino = str(mensaje.id_persona_destino)

        nodo_origen = self.nodo_fila[persona_origen]
        nodo_destino = self.nodo_fila[persona_destino]

        self.matriz_adyacencia[nodo_origen][nodo_destino] += 1
        self.matriz_adyacencia[nodo_destino][nodo_origen] += 1

        peso_arista = self.matriz_adyacencia[nodo_destino][nodo_origen]

        if len(self.max_aristas) == 0 or self.max_aristas[0] == peso_arista:
            self.max_aristas.append(Arista(nodo_origen, nodo_destino, peso_arista))
        elif self.max_aristas[0].peso < peso_arista:
            self.max_aristas = [Arista(nodo_origen, nodo_destino, peso_arista)]
        #elif self.max_aristas[0] == peso_arista:
            #self.max_aristas.append(Arista(nodo_origen, nodo_destino))

        # DETERMINAR SI PERSONA_ORIGEN O PERSONA_DESTINO AHORA SON LOS QUE MÁS CONEXIONES TIENEN

    def añadir_mensajes(self, mensajes):
        for mensaje in mensajes:
            self.añadir_mensaje(mensaje)

    # Retorna lo necesario para graficar el grafo graficado
    def retornar_grafo():
        pass