import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def mostrarGrafo(mAdyacencia):
    Grafo = nx.DiGraph()

    # Agregar nodos al grafo
    numNodos = len(mAdyacencia)
    
    Grafo.add_nodes_from(range(numNodos))

    #
    for i in range(numNodos):
        for j in range(numNodos):
            peso = mAdyacencia[i][j]
            if peso > 0:
                Grafo.add_edge(i, j, weight=peso)

    # Obtener posiciones de los nodos para la visualización
    pos = nx.spring_layout(Grafo)

    # Obtener pesos de los bordes
    pesosAristas = {(i, j): Grafo[i][j]['weight'] for i, j in Grafo.edges()}

    # Dibujar nodos y bordes ponderados
    nx.draw(Grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8, arrowsize=10)
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=pesosAristas)

    # Mostrar el gráfico
    plt.show()

# Ejemplo de matriz de adyacencia ponderada
matrizPonderada = [
    [0, 3, 2, 0, 7],
    [0, 0, 1, 4, 0],
    [0, 0, 0, 5, 1],
    [6, 0, 0, 0, 7]
]


# Dibujar el grafo ponderado
mostrarGrafo(matrizPonderada)

