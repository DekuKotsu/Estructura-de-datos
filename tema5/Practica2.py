#Algoritmo de ordenamiento interno
#nombre Quicksort
# que es un pivote
# como se elije un pivote
# cual es el quiterio de leccion del pivote con quicksort de los 4 criterios
import os 
os.system("cls")
class QuickSort:
    def __init__(self): 
        pass
    def ordenar(self, lista):

        pivote = lista[-1]
        mayores=[]
        menores=[]
        for i in lista[:-1]:
            if i <= pivote:
                menores.append(i)
            else:
                mayores.append(i)
        return (self.ordenar(menores) +[pivote]+ self.ordenar(mayores))

quick = QuickSort()
lista= [3,6,8,1]
print(quick.ordenar(lista))