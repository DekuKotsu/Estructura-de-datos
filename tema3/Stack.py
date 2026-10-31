class nodoStack(object):
    info, sig = None, None

class Stack(object):
    def __init__(self):
        self.__cima = None
        self.__tamanio = 0

    def apilar(self, dato):
        nodo = nodoStack()
        nodo.info = dato
        nodo.sig = self.__cima
        self.__cima = nodo
        self.__tamanio += 1

    def obtener_tamanio(self):
        return self.__tamanio

    def desapilar(self):
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
        return None

    def barrido(self):
        paux = Stack()

        while not self.stack_void():
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)

        while not paux.stack_void():
            dato = paux.desapilar()
            self.apilar(dato)

    def buscar(self, dato):
        actual = self.__cima
        posicion = 1

        while actual is not None:
            if actual.info == dato:
                return posicion
            actual = actual.sig
            posicion += 1

        return -1

    def limpiar(self):
        self.__cima = None
        self.__tamanio = 0

    def elementos(self):
        actual = self.__cima

        if actual is None:
            print("La pila está vacía")
            return

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
pila.elementos()