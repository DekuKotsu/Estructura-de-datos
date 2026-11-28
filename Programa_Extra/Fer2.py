import os 
os.system("cls")

#while True:
#n=0
#while True:
#    aux=8
#    if n<=8:
#        print(n)
#        n+=1
#    else:
#        print(n)
#        break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# calcular el resultado de un estudiante
# solicitar el nombre y sus 3 calificaciones correspondientes a los parciales del semestre
# Debe cumplir con: si alguna calificacion es menor a 0 o mayor 100 
# 
#
#
#

#clase1 = int(input(""))
#
#clase2 = int(input(""))
#
#clase3 = int(input(""))
#



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Ciclos For

#n= int(input("Ingresa un numero:"))

#for i in range(10,1,2): # el ultimo numero puede incrementar o puede retroseder 
#    print(f"{n} * {i}= {n*i}")
#<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# solicita al ususario que ingrese un numero y calcule la suma de todos los numeros del 1 hasta el numero ingresado

n= int(input("Ingresa un numero:"))
secuencia = 0
for i in range(1,n+1):
    secuencia +=i # incremento

print(secuencia)

