import os 
os.system("cls")
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class CircularLinkedList:
    def __init__(self):
        self.cabeza = None
        self.tam = 0

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            aux = self.cabeza
            while aux.siguiente != self.cabeza:
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.siguiente = self.cabeza
        self.tam += 1

    def mostrar(self, pasos = 10):
        actual = self.cabeza    
        contador = 0
        while actual is not None and contador < pasos:
            print(f"{actual.dato} -> ", end="")
            actual = actual.siguiente
            contador += 1

circular_list = CircularLinkedList()
for i in range(1, 6):
    circular_list.insertar_inicio(i)
circular_list.mostrar(6)
