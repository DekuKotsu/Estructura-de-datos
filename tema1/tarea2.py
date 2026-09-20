import os, math
import numpy as np
os.system("cls")
#Regresion lineal
x = int(input("Introduce el número de puntos: "))
y= int(input("Introduce el número de puntos: "))
def regresion_lineal(x, y):
    n = x
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x * y)
    x2_mean = np.mean(x ** 2)

    m = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
    b = y_mean - m * x_mean

    return m, b

print(regresion_lineal(x, y))

