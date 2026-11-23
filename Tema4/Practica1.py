import os 
import matplotlib.pyplot as plt
import networkx as nx
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


    def agregar_nodos(self, nodo, grafo):
        if nodo is not None:
            grafo.add_node(nodo.dato)

            if nodo.izquierdo is not None:
                grafo.add_edge(nodo.dato, nodo.izquierdo.dato)
                self.agregar_nodos(nodo.izquierdo, grafo)

            if nodo.derecho is not None:
                grafo.add_edge(nodo.dato, nodo.derecho.dato)
                self.agregar_nodos(nodo.derecho, grafo)

    def graficar(self):
        grafo = nx.DiGraph()
        self.agregar_nodos(self.raiz, grafo)

        posiciones = {}
        contador = [0]

        def acomodar(nodo, nivel=0):
            if nodo is not None:
                acomodar(nodo.izquierdo, nivel + 1)
                posiciones[nodo.dato] = (contador[0], -nivel)
                contador[0] += 1
                acomodar(nodo.derecho, nivel + 1)

        acomodar(self.raiz)

        plt.figure(figsize=(12, 8))
        nx.draw(
            grafo,
            posiciones,
            with_labels=True,
            node_color="skyblue",
            node_size=1800,
            font_size=12,
            font_weight="bold",
            arrows=False
        )

        plt.axis("off")
        plt.show()


# Crear árbol
arbol = ArbolBinario()

# Insertar datos
# Crear nodos
A = Nodo("A")
B = Nodo("B")
M = Nodo("M")
C = Nodo("C")
D = Nodo("D")
N = Nodo("N")
O = Nodo("O")
E = Nodo("E")
F = Nodo("F")
G = Nodo("G")
H = Nodo("H")
P = Nodo("P")
Q = Nodo("Q")
I = Nodo("I")
J = Nodo("J")
K = Nodo("K")
L = Nodo("L")

# Conectar los nodos
arbol.raiz = A

A.izquierdo = B
A.derecho = M

B.izquierdo = C
B.derecho = D

C.izquierdo = E
C.derecho = F

F.derecho = I

D.izquierdo = G
D.derecho = H

H.derecho = J
J.derecho = K
K.derecho = L

M.izquierdo = N
M.derecho = O

O.izquierdo = P
O.derecho = Q
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
arbol.graficar()
#en la practica 163 hay que sacar las 3 tareas para equipos
