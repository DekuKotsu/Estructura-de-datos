#Tarea timsort investigar vale 60% investigar que lenguaje ocupan timsort,
# quien lo creo, para que lo creo, como se ocupa

class RadixSort:
    def __init__(self, lista):
        self.lista = lista.copy()

    def ordenar(self):
        maximo = max(self.lista)
        exp = 1
        while maximo // exp > 0 :
            n = len(self.lista)
            salida = [0] * n
            conteo = [0] * 10
            for numero in self.lista:
                digito = (numero // exp) % 10
                conteo[digito]+=1
            for i in range(1, 10):
                conteo[i] += conteo[i - 1]

            for i in range(n -1, -1, -1):
                numero = self.lista[i]

                digito = (numero//exp) % 10

                salida[conteo[digito]-1] = numero

                conteo[digito] -= 1
            self.lista = salida
            exp *= 10
        return self.lista

numero = [170, 45, 90, 802, 24, 2, 66]
radix = RadixSort(numero)

print(f"lista original: {numero}")
print(f"Lista ordenada: {radix.ordenar()}")
#En el reporte hacer tablas para explicar el funcionamiento