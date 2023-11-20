import networkx as nx
import matplotlib.pyplot as plt

def mostrarGrafo(mAdyacencia):

    Grafo = nx.Graph()
    numNodos = len(mAdyacencia)

    # Agregamos los nodos al grafo
    Grafo.add_nodes_from(range(numNodos))

    # Agregamos los pesos a las aristas
    for i in range(numNodos):
        for j in range(numNodos):
            peso = mAdyacencia[i][j]
            if peso > 0:
                Grafo.add_edge(i, j, weight=peso)

    # Metodo para que la visualización del grafo sea ordenada
    pos = nx.spring_layout(Grafo)

    # Obtener pesos de las aristas
    pesosAristas = {(i, j): Grafo[i][j]['weight'] for i, j in Grafo.edges()}

    # Dibujar el grafo con los nodos y los pesos de las aristas
    nx.draw(Grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8, arrowsize=10)
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=pesosAristas)

    # Mostrar el grafo
    plt.show()