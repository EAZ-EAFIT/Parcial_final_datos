from Mensaje import Mensaje

# Clase Arista con nodo origen, destino y peso de arista
class Arista:
    def __init__(self, nodo_origen, nodo_destino, peso):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.peso = peso

# Clase Nodo con objeto destino y grado
class Nodo:
    def __init__(self, objeto, grado):
        self.objeto = objeto
        self.grado = grado

# Clase grafo
class Grafo:

    def __init__(self, personas):

        # Lista con nodos y sus respectivos grados
        self.nodos = [Nodo(persona, 0) for persona in personas]

        # Listado de aristas con mayor peso
        self.max_aristas = []

        # Lista que registra nodos con mayor grado
        self.max_nodos = []

        # Matriz de adyacencia del grafo
        cantidad_nodos = len(personas)
        self.matriz_adyacencia = [[ 0 for j in range(cantidad_nodos)] for i in range(cantidad_nodos)]

    # Añade un mensaje a el grafo de relaciones, incrementando el peso o creando una nueva arista
    def añadir_mensaje(self, mensaje):

        # Se identifica emisor y receptor del mensaje con sus respectivos id
        persona_origen = mensaje.persona_origen
        persona_destino = mensaje.persona_destino

        # Obtener los indices de los nodos de origen y destino en la lista de nodos
        idx_origen = None
        idx_destino = None
        indice  = 0
        while indice < len(self.nodos) or idx_origen == None or idx_destino == None:
            if self.nodos[indice].objeto == persona_origen:
                idx_origen = indice
            elif self.nodos[indice].objeto == persona_destino:
                idx_destino = indice
            indice += 1

        nodo_origen = self.nodos[idx_origen]
        nodo_destino = self.nodos[idx_destino]

        """ Identificación de persona con más amigos """

        # Si no existe conexión entre emisor y receptor, se aumenta el grado de sus nodos
        if self.matriz_adyacencia[idx_origen][idx_destino] == 0:
            self.nodos[idx_origen].grado += 1
            self.nodos[idx_destino].grado += 1

            # Se valida si emisor tiene la mayor cantidad de conexiones
            if len(self.max_nodos) == 0 or self.max_nodos[0].grado == nodo_origen.grado:
                self.max_nodos.append(nodo_origen)
            elif self.max_nodos[0].grado < nodo_origen.grado:
                self.max_nodos = [nodo_origen]

            # Se valida si receptor tiene la mayor cantidad de conexiones
            if len(self.max_nodos) == 0 or self.max_nodos[0].grado == nodo_destino.grado:
                self.max_nodos.append(nodo_destino)
            elif self.max_nodos[0].grado < nodo_destino.grado:
                self.max_nodos = [nodo_destino]

        """ Identificación de conexión más fuerte """

        # Se incrementa peso de conexión entre emisor y receptor de mensaje
        self.matriz_adyacencia[idx_origen][idx_destino] += 1
        self.matriz_adyacencia[idx_destino][idx_origen] += 1

        peso_arista = self.matriz_adyacencia[idx_destino][idx_origen]

        # Se verifica si la nueva conexión es igual o mayor a la previa maxima, y de ser el caso se cambia
        if len(self.max_aristas) == 0 or self.max_aristas[0].peso == peso_arista:
            self.max_aristas.append(Arista(nodo_origen, nodo_destino, peso_arista))
        elif self.max_aristas[0].peso < peso_arista:
            self.max_aristas = [Arista(nodo_origen, nodo_destino, peso_arista)]

    def añadir_mensajes(self, mensajes):
        for mensaje in mensajes:
            self.añadir_mensaje(mensaje)

    # Imprime datos importantes del grado
    # MEJORAR
    def print_datos(self):
        print(self.max_aristas)
        for arista in self.max_aristas:
            print(f"{arista.peso}  entre {arista.nodo_origen.objeto.nombre} y {arista.nodo_destino.objeto.nombre}")
        for nodo in self.max_nodos:
            print(f"Maximo nodo: {nodo.objeto.nombre} {nodo.objeto.id} grado: {nodo.grado}")

    # Imprime el grafo como lista de adyacencia
    def print_grafo(self):
        pass