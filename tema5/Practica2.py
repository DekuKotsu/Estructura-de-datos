#Algoritmo de ordenamiento interno
#nombre Quicksort
# que es un pivote
# como se elije un pivote
# cual es el quiterio de leccion del pivote con quicksort de los 4 criterios
import os 
os.system("cls")
class QuickSort:
    def __init__(self, lista): 
        self.__lista = lista
    def ordenar(self, lista): #con listas de python 
        if len(lista) <= 1:
            return lista
        pivote = lista[-1]
        mayores=[]
        menores=[]
        for i in lista[:-1]:
            if i <= pivote:
                menores.append(i)
            else:
                mayores.append(i)
        return (self.ordenar(mayores) +[pivote]+ self.ordenar(menores))

    def ordenar_lista(self, inicio, fin): # con arreglos
        if inicio < fin:
            pivote = self.__lista[fin]
            i = inicio-1
            for j in range(inicio, fin):
                if self.__lista[j]<= pivote:
                    i+=1
                    self.__lista[i], self.__lista[j] = self.__lista[j], self.__lista[i]
            self.__lista[i+1], self.__lista[fin] = self.__lista[fin], self.__lista[i+1]
            posicion = i + 1
            self.ordenar_lista(inicio, posicion -1 )
            self.ordenar_lista(posicion+1, fin)
            return self.__lista
lista= [3,6,8,9,7,2,10]
quick = QuickSort(lista)
#print(quick.ordenar(lista))
print(quick.ordenar_lista(0,len(lista)-1)) 
