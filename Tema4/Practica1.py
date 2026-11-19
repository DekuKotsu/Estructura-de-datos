import os 
os.system("cls")
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
# Los datos pequeños van a la izquierda
# Los datos mayores van a la derecha
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar_recursivo(self.raiz, nuevo)

    def _insertar_recursivo(self, actual, nuevo):
        if nuevo.dato < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo
            else:
                self._insertar_recursivo(actual.derecho, nuevo)

    def altura(self, nodo):
        if nodo is None:
            return 0
        izquierda = self.altura(nodo.izquierdo)
        derecha = self.altura(nodo.derecho)
        return 1 + max(izquierda, derecha)

    def preorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(nodo.dato, end="")
            self.inorden(nodo.derecho)

    def inorden(self, nodo):
        if nodo is not None:
            print(f"{nodo.dato} ->", end="")
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierdo)
            self.postorden(nodo.derecho)
            print(nodo.dato, end="")
# Crear árbol
arbol = ArbolBinario()

# Insertar datos
arbol.insertar(6)
arbol.insertar(4)
arbol.insertar(8)
arbol.insertar(1)
arbol.insertar(5)
print("Altura del árbol:", arbol.altura(arbol.raiz))
print("\n""Recorrido en preorden")
arbol.preorden(arbol.raiz )
print("\n""Recorrido en inorden")
arbol.inorden(arbol.raiz)
print("\n""Recorrido en postorden")
arbol.postorden(arbol.raiz)
