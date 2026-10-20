class nodoStack(object):
    info, sig = None, None
class Stack(object):
    def __init__(self):
        self.__cima = None
        self.__tamanio = 0
    
    def apilar(self, dato): #pruebas de apilamiento
        nodo = nodoStack()
        nodo.info=dato
        nodo.sig =self.__cima
        self.__cima = nodo
        self.__tamanio += 1
    
    def obtener_tamanio(self):
        return self.__tamanio

    def desapilar(self): # 2 pruebas de desapilamineto
        if self.stack_void():
            return None 
        x = self.__cima.info
        self.__cima = self.__cima.sig
        self.__tamanio -= 1
        return x

    def stack_void(self):
        return self.__cima is None

    def en_cima(self):
        if self.__cima is not None:
            return self.__cima.info
        else: 
            return None

    def barrido(self):
        paux = Stack()
        while(not self.stack_void(self)):
            dato = self.desapilar(self)
            print(dato)
            self.apilar(paux,dato)
        while(not self.stack_void(paux)):
            dato  = self.desapilar(paux)
            self.apilar(self,dato)

    def buscar(self, dato): #1 de buscar
        actual = self.__cima
        posicion = 1
        while actual is not None:
            if actual.info == dato:
                actual = actual.sig
                posicion +=1

    def limpiar(self): #1 de limpiar 
        while not self.stack_void():
            self.desapilar()
            #otra forma
            #self.__cima = None
            #self.__tamanio = 0
    def elementos (self):
        actual = self.cima()
        if actual is None:
            print("La pila esta vacia")
        if actual is None:
            print("La pila esta vacia")
        while actual is not None:
            print(f"| {actual.info} |")
            actual = actual.sig

    def __str__(self):
        return f"""
cima: {self.__cima}
tamanio: {self.__tamanio}
"""
    
pila= Stack()
pila.apilar(22)
pila.apilar(23)
pila.apilar(24)
pila.apilar(25)
pila.apilar(26)

