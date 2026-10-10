#Ejercicio 10
n = int(input("Ingrese un número entero positivo: "))
def cantidad_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + cantidad_digitos(n // 10)

print(f"La cantidad de dígitos en {n} es: {cantidad_digitos(n)}")