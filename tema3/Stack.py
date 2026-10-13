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

    
    def __str__(self):
        return f"""
cima: {self.__cima}
tamanio: {self.__tamanio}
"""
pdatos= Stack()
ppar = Stack()
pimpar = Stack()

print(pdatos)
print(ppar)
print(pimpar)