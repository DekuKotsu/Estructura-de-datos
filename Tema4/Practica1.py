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
            print(f"{nodo.dato} -> ", end="")
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)
    
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(f"{nodo.dato} -> ", end="")
            self.inorden(nodo.derecho)
    
    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierdo)
            self.postorden(nodo.derecho)
            print(f"{nodo.dato} -> ", end="")
    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return (1+ self.contar_nodos(nodo.izquierdo) + self.contar_nodos(nodo.derecho)) 
    def contar_hojas(self, nodo):
        if nodo is None:
            return 0 
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1
        return (self.contar_hojas(nodo.izquierdo)+ self.contar_hojas(nodo.derecho))
    def obtener_hojas(self, nodo, hojas=None):
        if hojas is None:
            hojas = []
        if nodo is not None:
            if nodo.izquierdo is None and nodo.derecho is None:
                hojas.append(nodo.dato)
            self.obtener_hojas(nodo.izquierdo, hojas)
            self.obtener_hojas(nodo.derecho, hojas)
        return hojas
    def nodo_internos(self, nodo, internos=None):
        if internos is None:
            internos=[]
        if nodo is not None:
            if nodo.izquierdo is not None or nodo.derecho is not None:
                internos.append(nodo.dato)
            self.nodo_internos(nodo.izquierdo, internos)
            self.nodo_internos(nodo.derecho, internos)
        return internos
# Crear árbol
arbol = ArbolBinario()

# Insertar datos
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(6)
arbol.insertar(8)
arbol.insertar(4)
arbol.insertar(10)
print("Altura del árbol:", arbol.altura(arbol.raiz))
print("\n""Recorrido en preorden")
arbol.preorden(arbol.raiz )
print("\n""Recorrido en inorden")
arbol.inorden(arbol.raiz)
print("\n""Recorrido en postorden")
arbol.postorden(arbol.raiz)
print()
print("Nodos", arbol.contar_nodos(arbol.raiz))
print("Hojas:", arbol.contar_hojas(arbol.raiz))
print("Obtener Hojas:", arbol.obtener_hojas(arbol.raiz))
print("obtener nodos internos:",arbol.nodo_internos(arbol.raiz))
