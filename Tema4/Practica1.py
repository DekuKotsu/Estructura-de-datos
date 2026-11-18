class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
#el criterio que se va acupar que los datos pequeños va a la izquierda y a la derecha van lo que sean mayores
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insentar_recursivo(self.raiz, nuevo)

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

arbol = ArbolBinario()
arbol.insertar(6)
arbol.insertar(4)
arbol.insertar(2)
arbol._insertar_recursivo(4)
arbol._insertar_recursivo(2)
arbol.altura()