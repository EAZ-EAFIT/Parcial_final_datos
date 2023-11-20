import Dummy
from Grafo import *
import Salida
import Persona

def main():
    num_personas = 10
    num_mensajes = 100

    personas = Persona.generar_personas(num_personas)

    mensajes = Dummy.generar_mensajes(personas, num_mensajes)

    grafo = Grafo(personas)
    grafo.añadir_mensajes(mensajes)

    # Imprimir mensajes
    for mensaje in mensajes:
        print(mensaje)
        print()

    grafo.print_datos()

    Salida.mostrarGrafo(grafo.matriz_adyacencia)

main()