import os
import numpy as np
os.system("cls")
A = np.array([[1, 2, 3], [4, 2, 6], [7, 8, 9]])
B = np.array([[6, 8, 6], [6, 9, 4], [3, 11, 8]]) 
print("Matriz A:")
print(A)
print("Matriz B:")
print(B)
#operaciones con matrices
print("Suma de matrices A + B:")
print(A + B)
print("Resta ")
print(A - B)
print("Multiplicacion")
#multiplicacion de elementos por elemento
print(A * B)
print("Multiplicacion matricial")
#multiplicacion matricial
print(A @ B)
#con numpy se puede hacer la multiplicacion matricial de dos maneras
print(np.matmul(A, B))
print(np.dot(A, B))
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
#producto punto
print(f"producto punto: {v1 @ v2}")
#Producto cruz
print(f"producto cruz: {np.cross(v1, v2)}")
#Determinante de una matriz 
#para la determinar una matriz debe de ser cuadrada
print(f"Determinante de la matriz A: {np.linalg.det(A)}")
print(f"Determinante de la matriz B: {np.linalg.det(B)}")
#inversa de una matriz
print(f"Inversa de la matriz A: {np.linalg.inv(A)}")
print(f"Inversa de la matriz B: {np.linalg.inv(B)}")
#Concepto, si multiplicamos la inversa por la identidad nos da la matriz original
#queda pendiente A =A^-1 * I
print(A @ np.linalg.inv(A))
print("Matriz identidad:")
print(np.eye(3))
#Rango de una matriz 
print(f"Rango de la matriz A: {np.linalg.matrix_rank(A)}")
print(f"Rango de la matriz B: {np.linalg.matrix_rank(B)}")
#invera de una matriz
#A * A^-1 = I
"""
Realizar el producto de la matriz A por su inversa
y demostrar que da la identidad
¿Que representa el rango de una matriz?
2x+y=5
x+3y=6
los valores se tienen que crear una matriz de 2x2
"""
C = np.array([[2,1], [1,3]])
v3 = np.array([5,6])
x = np.linalg.solve(C,v3)
print(f"La solucion del sistemas de ecuaciones es {x[0]}")
print(f"La solucion del sistemas de ecuaciones es {x[1]}")
"""
Proponer un sistemas de ecuacion de 3x3 y hayar la solucion 
El resultado debe decir
"la solucion de x es :"
"La solucion de y es:"
"La solucion de z es:"
"""
"""
x + y + z= 8
x-2y+z=4
x+y-z=-4
"""
B =np.array([[1,1,1], [1,-2,1], [1,1,-1]])
v4 =np.array([8,4,-4])
X = np.linalg.solve(B,v4)
print(f"La solucion del sistemas de ecuaciones de 3x3 es {X[0]:.2f}")
print(f"La solucion del sistemas de ecuaciones de 3x3 es {X[1]:.2f}")
print(f"La solucion del sistemas de ecuaciones de 3x3 es {X[2]:.2f}")

