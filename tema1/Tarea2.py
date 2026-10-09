import os, math
import numpy as np
os.system("cls")
#Regresion lineal
X=[500, 700, 800, 600, 400, 500, 600, 800]
Y = [84, 75, 99, 72, 69, 81, 63, 93]
n = len(X)
X_suma= sum(X)
Y_suma = sum(Y)

suma_XY = 0
suma_X2 = 0
suma_Y2 = 0
for i in range(n):
    suma_XY += X[i]*Y[i]
    suma_X2 += pow(X[i],2)
    suma_Y2 += pow(Y[i],2)
numerador = n * suma_XY - X_suma * Y_suma
denominador = math.sqrt(
(n * suma_X2 - X_suma ** 2) * (n * suma_Y2 - Y_suma ** 2)
)
b = (n * suma_XY -(X_suma * Y_suma)) /( n*suma_X2 - pow(X_suma, 2))
a = (Y_suma/n)-b*(X_suma/n)
r = numerador / denominador
r2 = pow(r,2)
nuevax= 800
Y = a +b*nuevax
t = ((r*math.sqrt(n-2))/math.sqrt(1-pow(r,2)))
print(f"Coeficiente de correlacion: {r:.3f}")
print(f"Coeficiente de correlacion^2 {r2:.3f}")
print(f"prueba del valor estadistico: {t:.3f}")
print(f"Pendinete b: {b:.5f}")
print(f"Interseccion a: {a}")
print(f"Y´={a}+ {b:.5f}X")
print(f"y´= {Y:.2f}")
