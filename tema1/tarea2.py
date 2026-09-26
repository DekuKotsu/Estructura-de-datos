import os, math
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
    (n * suma_X2 - X_suma ** 2) *
    (n * suma_Y2 - Y_suma ** 2)
)

division = numerador / denominador

print(f"Coeficiente de correlacion: {division:.3f}")