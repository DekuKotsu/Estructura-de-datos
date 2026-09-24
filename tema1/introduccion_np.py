#arrays de 2 dimenciones con numpy 
import os
import numpy as np
os.system("cls")
#numpy nos va ayudar para mejorar el rendimiento de la memoria
matriz =np.array([[10,8,2], [3,1,2], [5,4,9]], dtype=int)
#array son para arreglos de una a tres dimesiones
print(matriz)
print(np.ones((2,2)))#.ones nos ayuda a crear matrices con todos los elementos con uno
print(np.zeros((2,2)))
print(np.full((2,2),5))
#.full llena la matriz con un numero dado (numeros complejos, flortantes,numeros reales)
print(np.empty((2,2)))
#.empty da una matriz vacia
print(np.eye(5))
#.eye da la matriz identidad
print(np.identity(5))
print(np.diag([10,9,2]))
#.diag hace la diagonal
print(np.arange(12).reshape(3,4))
#.arange, .reshape crea una matriz nxn con valores de 1 al 12 o mas con ahi se puede ir cambiando
print(matriz.shape)
print(matriz.ndim)
print(matriz.size)
print(matriz.dtype)
print(matriz[0,:])
print(matriz[1,:])
print(matriz[-1,:])
print(matriz [:,0])
print(matriz [:,1])
print(matriz [:,-1])
print(matriz [0:2,:])
print(matriz [:,1:3])
print(matriz [0:2,1:3])
matriz[2,1] =0  # para modificar un elemento
print(matriz)
matriz[0,:]= [4,2,9] #para modificar la fila completa 
print(matriz)
matriz[:,1]= [7,7,7] #para modificar la columna completa
print(matriz)