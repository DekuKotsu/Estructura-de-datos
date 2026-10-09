#Regresion lineal con numpy
import os, math
import numpy as np
os.system("cls")
X = np.array([500,700,800, 600, 400, 500, 600, 800], dtype=int)
Y = np.array([84, 75, 99, 72, 69, 81, 63, 93],dtype=int)
X_suma = np.sum(X)
Y_suma = np.sum(Y)
n = len(X)
xy = 0
x2 = 0
y2 = 0
for i in range(n):
    xy += X[i] * Y[i]
    x2 += pow(X[i],2)
    y2 += pow(Y[i],2)
r= np.corrcoef(X,Y)[0,1]
r2 = pow(r,2)
#prueba de valor estadistico
t=((r*math.sqrt(n-2)/math.sqrt(1-r2)))
#pendiente
b = (n * xy -(X_suma * Y_suma)) /( n*x2 - pow(X_suma, 2))
#intepceccion
a = (Y_suma/n)-b*(X_suma/n)
#y´
def y_prima():
    new_X = 800
    y = a+b*new_X
    return y
print(f"Coeficiente de correlacion: {r:.3f}")
print(f"Coeficiente de correlacion^2 {r2:.3f}")
print(f"prueba del valor estadistico: {t:.3f}")
print(f"Pendinete b: {b:.5f}")
print(f"Interseccion a: {a}")
print(f"Y´={a}+ {b:.5f}X")
print(f"y´= {y_prima():.2f}")