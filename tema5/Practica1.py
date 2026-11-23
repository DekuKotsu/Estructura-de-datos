class BubbleSort:
    def __init__(self, datos):
        self.datos = datos

    def ordenar(self):
        n = len(self.datos)
        for i in range(n):
            for j in range(n-i-1):
                if self.datos[j]> self.datos[j+1]:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j+1]
                    self.datos[j + 1] = aux
        return self.datos
