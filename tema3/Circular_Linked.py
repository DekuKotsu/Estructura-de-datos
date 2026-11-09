import os
import random 
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

    def tamanio(self):
        return f"El tamanio de la lista es: {self.tam}"

    def lista_void(self):
        return self.cabeza is None

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.lista_void():
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            aux = self.cabeza
            while aux.siguiente != self.cabeza:
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.siguiente = self.cabeza
        self.tam += 1
        return f"Elemento insertado: {dato}"

    def mostrar(self, pasos=10): 
        actual = self.cabeza 
        contador = 0
        while actual is not None and contador < pasos:
            print(f"{actual.dato} -> ", end="")
            actual = actual.siguiente
            contador += 1
        print("... (circular)")

    def insertar_medio(self, dato, posicion):
        if posicion < 0 or posicion > self.tam:
            return "Posicion fuera de rango"
        if posicion == 0:
            self.insertar_inicio(dato)
        else:
            nuevo = Nodo(dato)
            aux = self.cabeza
            for _ in range(posicion - 1):
                aux = aux.siguiente
            nuevo.siguiente = aux.siguiente
            aux.siguiente = nuevo
            self.tam += 1
        return f"Elemento insertado: {dato}"

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
            while aux.siguiente != self.cabeza:
                aux = aux.siguiente
            return aux.dato

    def limpiar(self):
        self.cabeza = None
        self.tam = 0

    def buscar(self, dato):
        if self.lista_void():
            return "La lista esta vacia"
        else:
            aux = self.cabeza
            posicion = 0
            while True:
                if aux.dato == dato:
                    return f"Elemento {dato} encontrado en la posicion {posicion}"
                aux = aux.siguiente
                posicion += 1
                if aux == self.cabeza:
                    break
            return f"Elemento {dato} no encontrado en la lista"

    def invertir(self):
        if self.lista_void():
            return "La lista esta vacia"
        else:
            prev = None
            current = self.cabeza
            next_node = None
            first_node = self.cabeza
            while True:
                next_node = current.siguiente
                current.siguiente = prev
                prev = current
                current = next_node
                if current == first_node:
                    break
            self.cabeza.siguiente = prev
            self.cabeza = prev

    def contar_elementos(self, dato):
        if self.lista_void():
            return 0
        else:
            aux = self.cabeza
            contador = 0
            while True:
                if aux.dato == dato:
                    contador += 1
                aux = aux.siguiente
                if aux == self.cabeza:
                    break
            return contador

circular_list = CircularLinkedList()
rango = random.randint(1, 10)
for i in range(rango):
    numero = random.randint(1, 100)
    circular_list.insertar_inicio(numero)
print(circular_list.tamanio())
circular_list.mostrar(6)
circular_list.insertar_final(6)
circular_list.mostrar(10)
circular_list.insertar_medio(99, 3)
circular_list.mostrar(8)
print(circular_list.buscar(99))
print(circular_list.buscar(100))
print(f"El numero de elementos de 99 es: {circular_list.contar_elementos(99)}")
print(circular_list.primer_elemento())
print(circular_list.ultimo_elemento())
circular_list.invertir()
circular_list.mostrar(10)
#circular_list.limpiar()