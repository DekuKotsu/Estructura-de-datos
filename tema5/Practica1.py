import os
os.system("cls")
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

numero = [8, 2, 5, 9, 3, 1, 7]
bubble = BubbleSort(numero)
print(bubble.ordenar())

nombres = ["Carlos", "Ana", "Pedro", "Luis", "Beatriz"]
bubble1 = BubbleSort(nombres)
print(bubble1.ordenar())

#investigar la complegidad computacional de big O del metodo de la burbuja
