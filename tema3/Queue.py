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
        self.frente = self.frente.info
        self.tamanio -=1
        if self.frente is None:
            self.final = None
        return x

cola1 = Queue()
#print(cola1)
#    print("Cola vacia")
#else:
#    print("Contiene datos")
cola1.en_colar(3)
cola1.en_colar(5)
print(f"Tamaño de la cola: {cola1.obtener_tamanio()}")
print(f"{cola1.desencolar()}")