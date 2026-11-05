"tema 3 estructuras lineales"
"subtema 3.3.2"
"nombre de la pracctica listas enlazadas"
import os 
os.system("cls")
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None
        self.tam = 0
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tam += 1
    def tamanio(self):
        return f"El tamanio de la lista es: {self.tam}"
    def lista_void(self):
        return self.cabeza is None
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.lista_void():
                self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux= aux.siguiente
            aux.siguiente = nuevo
        self.tam+=1
    def mostrar(self):
        if self.lista_void():
            return "La lista esta vacia"
        else:
            aux = self.cabeza
            while aux is not None:
                print(f"{aux.dato} -> ", end="", )
                aux = aux.siguiente
            print("None")
    def insertar_medio(self,dato, posicion):
        if posicion < 0 or posicion > self.tam:
            return "Posicion fuera de rango"
        nuevo = Nodo(dato)
        if posicion == 0:
            self.insertar_inicio(dato)
        else:
            aux = self.cabeza
            for _ in range(posicion - 1):
                aux = aux.siguiente
            nuevo.siguiente = aux.siguiente
            aux.siguiente = nuevo
            self.tam += 1
    def __str__(self):
        return f"""

"""


lista = ListasEnlazadas()
lista.insertar_inicio(3)
lista.insertar_inicio(5)
print(lista.tamanio())
print(lista.lista_void())
lista.insertar_final(4)
lista.mostrar()
lista.insertar_medio(10, 1)
lista.mostrar()