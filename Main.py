import Dummy
from Grafo import *
import Salida
import Persona

def main():
    #Definimos el numero de personas y mensajes que vamos a generar
    num_personas = 4
    num_mensajes = 3

    #Generamos los arreglo con las personas correspondientes y los mensajes
    personas = Persona.generar_personas(num_personas)

    mensajes = Dummy.generar_mensajes(personas, num_mensajes)

    grafo = Grafo(personas)
    grafo.añadir_mensajes(mensajes)

    # Imprimir mensajes
    for mensaje in mensajes:
        print(mensaje)
        print()

    grafo.print_datos()
    print(grafo.matriz_adyacencia)
    for i in grafo.max_nodos:
        print(i.objeto.nombre)
    Salida.mostrarGrafo(grafo.matriz_adyacencia, personas)

main()