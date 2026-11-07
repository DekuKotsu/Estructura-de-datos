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

    def mostrar(self, pasos = 10):
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
                    return f"\n Elemento {dato} encontrado en la posicion {posicion}"
                aux = aux.siguiente
                posicion += 1
                if aux == self.cabeza:
                    break
            return f"Elemento {dato} no encontrado en la lista"

circular_list = CircularLinkedList()
for i in range(1, 6):
    circular_list.insertar_inicio(i)
circular_list.mostrar(6)
circular_list.insertar_final(6)
circular_list.mostrar(7)
circular_list.insertar_medio(99, 3)
circular_list.mostrar(8)
print(circular_list.buscar(99))
circular_list.buscar(100)
