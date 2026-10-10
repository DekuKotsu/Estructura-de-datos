# Ejercicio 4
#potencia
#Implementar una función para calcular 
# la potencia dado dos números enteros, el primero 
# representa la base y segundo el exponente
try:
    n1 = int(input("Ingrese la base: "))
    n2 = int(input("Ingrese el exponente: "))
except ValueError:
    print("Se debe de ingresar un numero entero positivo")
    exit()

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
print(f"{n1} elevado a la {n2} es: {potencia(n1, n2)}")