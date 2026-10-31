import os
from Queue import Queue #la importacion de otro archivo y su clase 
os.system("cls")
cola = Queue()
while True:
    print("==OPCIONES DE LA COLA ==")
    print("1.- Agregar al cliente")
    print("2.- Atender al cliente")
    print("3.- Mostrar clientes de la cola")
    print("4.- Mostrar el siguente por atender")
    print("5.- Total de clientes en espera")
    print("6.- Salir")
    try:
        op = int(input("Eligue una opcion: "))
    except ValueError:
        print ("Ocupe un valor de tipo entero")
        continue #Para que continue el programa desde el inicio

    if op == 1:
        nom = input("Ingresa el nombre del cliente: ")
        cola.en_colar(nom)
        print("Nombre añadido a la cola")
    elif op == 2:
        cola.desencolar()
        print("Cliente atendido con exito")
    elif op ==3:
        print("Personas en la fila:")
        cola.mostrar_elementos()
    elif op == 4:
        print("Siguiente cliente: ")
        print(cola.en_frente())
    elif op == 5:
        print(f"El total de clientes en espera es: {cola.obtener_tamanio()}")
    elif op == 6:
        print("Salida del programa..")
        break
    else:
        print("Opcion no valida")

"el problema 10 de las colas en la pagina 95 esta es la tarea 2"

