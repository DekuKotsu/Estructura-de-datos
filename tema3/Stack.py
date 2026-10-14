class nodoStack(object):
    info, sig = None, None
class Stack(object):
    def __init__(self):
        self.__cima = None
        self.__tamanio = 0
    
    def apilar(Stack, dato):
        nodo = nodoStack()
        nodo.info=dato
        nodo.sig =Stack.__cima
        Stack.cima = nodo
        Stack.__tamanio += 1
    
    def obtener_tamanio(self):
        return self.__tamanio

    def desapilar(self):
        x = Stack.cima.info()
        Stack.cima = Stack.cima.sig
        Stack.__tamanio -= 1
        return x

    def stack_vod(self):
        return Stack.cima is None

    def en_cima(self):
        if Stack.cima is not None:
            return Stack.cima.info
        else: 
            return None

    def __str__(self):
        return f"""
cima: {self.__cima}
tamanio: {self.__tamanio}
"""
    
pdatos= Stack()
ppar = Stack()
pimpar = Stack()
print(f"Tamaño pila {pdatos.obtener_tamanio()}")
print(f"Tamaño pila {ppar.obtener_tamanio()}")
print(f"Tamaño pila {pimpar.obtener_tamanio()}")
#subtema es pilas