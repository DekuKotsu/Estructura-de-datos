#factorial y figonazi con recursividad
#Practica1
import os, math
import time
import tracemalloc #este es para la memoria ram
import psutil #este es para la memoria ram
os.system("cls")
# adaptar el codigo para numeros negativos
def factorial(n):
    if(n == 0):
        return 1 #aqui retornara 1 si el numero es 0
    else:
        return n * factorial(n-1) #aqui se llama a la funcion de forma recursiva

def factorial_sin_recursividad(n):
    fac=1
    for i in range(1, n+1):
        fac *= i #aqui se calcula el factorial de forma no recursiva
    return f"Calcula de factorial de {n}! sin recusividad: {fac}"

def fibonacci(n):
    if (n ==0 or n==1): 
        return n #retornara el numero dado si es 0 o 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) #aqui se llama a la funcion de forma recursiva para calcular el fibonacci

def fibonacci_sin_recursividad(n):
    a = 0 
    b = 1
    for i in range(n):
        temp = b #almacena el valor de b en una variable temporal
        b = a+b #actulizamos el valor de b 
        a = temp #le damos el valor inicial de b para seguir con la secuencia
    return f"Calcula de fibonacci de {n} sin recusividad: {a}"
def medir_memoria(funcion, n):
    tracemalloc.start() #inicia la medicion de memoria
    factorial(n) #llama a la funcion factorial
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory() #obtiene la memoria actual y la maxima utilizada
    tracemalloc.stop() #detiene la medicion de memoria
    return memoria_actual, memoria_pico #retorna la memoria actual y la maxima utilizada

try: #Es para capturar el error de valor negativo
    n = int(input("Introduce un numero entero: "))
    if n < 0:
        raise ValueError("El numero debe ser positivo") #si el numero es negativo se lanza un error 
    else:
        print("Factorial")
        print(f"El factorial de {n}! es: {factorial(n)} con recursividad")
        print(factorial_sin_recursividad(n))
        print(f"El factorial de {n}! con math es: {math.factorial(n)}")
        print("-"*50)
        print("Fiboncci")
        print(f"El fibonacci de {n} es: {fibonacci(n)} con recursividad")
        print(fibonacci_sin_recursividad(n)) 
        print(f"El fibonacci de {n} con math es: {math.factorial(n)}")
except ValueError:
    print("Se debe de ingresar un numero entero positivo")
# en la pagina 24 hay estan las tareas tenemos que agarrar 8 problemas pero de forma 
# si son pares o impares y de forma recursiva y no recursiva
print("-"*50)
print("==========Factorial==========")
#Tiempo de ejecucion
inicio = time.perf_counter()
factorial_sin_recursividad(n)
fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio} segundos")

inicio = time.perf_counter()
factorial(n)
fin = time.perf_counter()
print(f"Iterativo: {fin - inicio} segundos")

print(f"Recursivo: {fin - inicio} segundos")

actual, pico = medir_memoria(factorial, n) 
print("iterativo")
print(f"Memoria actual: {actual} bytes")
print(f"Memoria pico: {pico} bytes")
#consumo de memoria RAM
actual, pico = medir_memoria(factorial_sin_recursividad, n) 
print("Recursivo")
print(f"Memoria actual: {actual} bytes")
print(f"Memoria pico: {pico} bytes")
# Consumo de CPU
proceso = psutil.Process()
proceso.cpu_percent(interval=None)
factorial(n)
cpu_recursivo = proceso.cpu_percent(interval=1)

proceso.cpu_percent(interval=None)
factorial_sin_recursividad(n)
cpu_iterativo = proceso.cpu_percent(interval=1)
#Resultado
print(f"Consumo de CPU (Recursivo): {cpu_recursivo:.2f}%")
print(f"Consumo de CPU (Iterativo): {cpu_iterativo:.2f}%")
#Para Fibnacci
print("-"*50)
print("==========Fiboncci==========")
#Tiempo de ejecucion
inicio = time.perf_counter()
fibonacci_sin_recursividad(n)
fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio} segundos")

inicio = time.perf_counter()
fibonacci(n)
fin = time.perf_counter()
print(f"Iterativo: {fin - inicio} segundos")

print(f"Recursivo: {fin - inicio} segundos")
actual, pico = medir_memoria(fibonacci, n) 
print("iterativo")
print(f"Memoria actual: {actual} bytes")
print(f"Memoria pico: {pico} bytes")
#consumo de memoria RAM
actual, pico = medir_memoria(fibonacci_sin_recursividad, n) 
print("Recursivo")
print(f"Memoria actual: {actual} bytes")
print(f"Memoria pico: {pico} bytes")

# Consumo de Cpu
proceso = psutil.Process()
proceso.cpu_percent(interval=None)
fibonacci(n)
cpu_recursivo = proceso.cpu_percent(interval=1)

proceso.cpu_percent(interval=None)
fibonacci_sin_recursividad(n)
cpu_iterativo = proceso.cpu_percent(interval=1)
#Resultado
print(f"Consumo de CPU (Recursivo): {cpu_recursivo:.2f}%")
print(f"Consumo de CPU (Iterativo): {cpu_iterativo:.2f}%")