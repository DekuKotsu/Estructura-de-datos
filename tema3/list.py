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
    def primer_elemento(self):
        if self.lista_void():
            return "none"
        else:
            return self.cabeza.dato 
    def ultimo_elemento(self):
        if self.lista_void():
            return "none"
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente
            return aux.dato
    def limpiar(self):
        self.cabeza = None
        self.tam = 0

    def invertir(self):
        if self.lista_void():
            return "La lista esta vacia"
        else:
            aux = self.cabeza
            prev = None
            while aux is not None:
                next_node = aux.siguiente
                aux.siguiente = prev
                prev = aux
                aux = next_node
            self.cabeza = prev

    def contar_elementos(self, dato):
        if self.lista_void():
            return 0
        else:
            aux = self.cabeza
            contador = 0
            while aux is not None:
                if aux.dato == dato:
                    contador += 1
                aux = aux.siguiente
            return contador

    def eleminar_inicio(self):
        if self.lista_void():
            return "La lista esta vacia"
        else:
            self.cabeza = self.cabeza.siguiente
            self.tam -= 1

    def eliminar_final(self):
        if self.lista_void():
            return "La lista esta vacia"
        else:
            aux = self.cabeza
            if aux.siguiente is None:
                self.cabeza = None
            else:
                while aux.siguiente.siguiente is not None:
                    aux = aux.siguiente
                aux.siguiente = None
            self.tam -= 1

    def eliminar_medio(self, posicion):
        if self.lista_void():
            return "La lista esta vacia"
        if posicion < 0 or posicion >= self.tam:
            return "Posicion fuera de rango"
        if posicion == 0:
            self.eleminar_inicio()
        else:
            aux = self.cabeza
            for _ in range(posicion - 1):
                aux = aux.siguiente
            aux.siguiente = aux.siguiente.siguiente
            self.tam -= 1

    def modificar_elemento(self, posicion, nuevo_dato):
        if self.lista_void():
            return "La lista esta vacia"
        if posicion < 0 or posicion >= self.tam:
            return "Posicion fuera de rango"
        aux = self.cabeza
        for _ in range(posicion):
            aux = aux.siguiente
        aux.dato = nuevo_dato

    def eliminar_elemento(self, dato):
        if self.lista_void():
            return "La lista esta vacia"
        aux = self.cabeza
        prev = None
        while aux is not None:
            if aux.dato == dato:
                if prev is None:
                    self.cabeza = aux.siguiente
                else:
                    prev.siguiente = aux.siguiente
                self.tam -= 1
                return
            prev = aux
            aux = aux.siguiente
        return "Elemento no encontrado"
"""
anexar eliminar al inicio, al final y en medio, buscar un elemento, modificar un elemento
investigar que son y una lista doblemente enlazada
que son las listas circulares  y un ejemplo
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
print(f"El primer elemento es: {lista.primer_elemento()}")
print(f"El ultimo elemento es: {lista.ultimo_elemento()}")
lista.mostrar()
lista.invertir()
lista.mostrar()
lista.insertar_final(3)
lista.mostrar()
print(f"El numero de elementos es: {lista.contar_elementos(3)}")