import Dummy
from Grafo import *
import Salida

cantidad_nodos = 10
cantidad_mensajes = 100
mensajes = Dummy.lista_mensajes(cantidad_mensajes, cantidad_nodos)
grafo = Grafo([str(i+1) for i in range(cantidad_nodos)])

grafo.añadir_mensajes(mensajes)
print(grafo.matriz_adyacencia)

for mensaje in mensajes:
    print(mensaje)
    print()

print("Max Arista: ", grafo.max_aristas[0].peso)
Salida.mostrarGrafo(grafo.matriz_adyacencia)