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

    # Guardar mensajes en un archivo de texto
    with open('Registro_Mensajes.txt', 'w', encoding="utf-8") as archivo_registro:
        for mensaje in mensajes:
            # Escribir mensaje en archivo de registro
            archivo_registro.write(str(mensaje) + '\n\n')

    grafo.print_datos()
    grafo.print_grafo()
    Salida.mostrarGrafo(grafo.matriz_adyacencia, personas)

main()