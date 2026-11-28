import os
os.system("cls")
class MergeSort:

    def ordenar(self, lista):
        if len(lista) <= 1:
            return lista
        mitad = len(lista)//2
        izquierda = self.ordenar(lista[:mitad])
        derecha = self.ordenar(lista[mitad:])
        return self.mezclar(izquierda, derecha)

    def mezclar(self, izquierda, derecha):
        resultado = []
        i = 0 
        j = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j+= 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

lista = [3, 9, 10, 1, 8, 7, 5, 2]
merge = MergeSort()
resultado = merge.ordenar(lista)
print(f"La lista ordenada es: {resultado}")

#un solo programa que incluye toda la materia
#El lunes