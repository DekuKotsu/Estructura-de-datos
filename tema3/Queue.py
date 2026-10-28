""" 
Coleccion es la que trabaja con python
"""
import os 
os.system("cls")
class nodoCola(object):
    info, sig = None, None

class Queue(object):
    def __init__(self): #constructor
        self.frente = None #no contiene nada en ningun tipo de datos
        self.final = None
        self.tamanio = 0

    def __str__(self):
        return f"Tamaño: {self.tamanio}"
    def cola_vacia(self):
        return self.frente is None
    def en_frente(self):
        if self.frente is not None:
            return self.frente.info
        return None
    
    def obtener_tamanio(self):
        return self.tamanio
    
    def en_colar(self, dato):
        nodo = nodoCola()   
        nodo.info = dato
        nodo.sig = None
        if self.cola_vacia():
            self.frente = nodo
            self.final = nodo
        else:
            self.final.sig = nodo
            self.final = nodo
        self.tamanio += 1

    def desencolar(self):
        if self.cola_vacia():
            return None 
        x = self.frente.info
        self.frente = self.frente.sig
        self.tamanio -=1
        if self.frente is None:
            self.final = None
        return x
    
    def buscar(self, dato):
        actual = self.frente
        posicion = 1
        while actual is not None:
            if actual.info == dato:
                return posicion
            actual = actual.sig
            posicion += 1
        return -1

    def limpiar(self):
        self.frente = None
        self.final = None
        self.tamanio = 0
#el none reserva todos los tipo de datos para cuando se le asigne algo
    def mostrar_elementos(self):
        actual = self.frente
        if actual is None:
            print("La cola esta vacia")
            return
        while actual is not None:
            print(f"|{actual.info}|")
            actual = actual.sig


cola1 = Queue()
#print(cola1)
#    print("Cola vacia")
#else:
#    print("Contiene datos")
cola1.en_colar(3)
cola1.en_colar(5)
cola1.en_colar(4)
print(f"Tamaño de la cola: {cola1.obtener_tamanio()}")
print(f"{cola1.desencolar()}")
print(f"El dato que buscas es{3} y esta en la posicion{cola1.buscar(2)}")
#print(cola1.limpiar())
#print(f"Tamaño de la cola: {cola1.obtener_tamanio()}")
cola1.mostrar_elementos()