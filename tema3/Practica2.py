import os
from Queue import Queue 
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
        nom = input("Ingresa el nombre del cliente ")
        cola.en_colar(nom)
        print("Nombre añadido a la cola")
    elif op == 2:
        cola.desencolar()

    elif op ==3:
        pass
    elif op == 4:
        pass
    elif op == 5:
        print(f"El total de clientes en espera es: {cola.obtener_tamanio()}")
    elif op == 6:
        print("Salida del programa..")
        break
    else:
        print("Opcion no valida")

