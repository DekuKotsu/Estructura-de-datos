import os, math
os.system("cls")
#tipos de datos en python
#cuanto espacio consume cada tipo de dato en memoria
ang = float(input("Introduce el valor de angulo: "))
Rad = math.radians(ang)
print("angulo en radianes: ", Rad)
print("angulo en grados: ", ang)
print("seno", ang, "=", math.sin(Rad))
print("coseno", ang, "=", math.cos(Rad))
#Seno
serie = 0
flag = True
for i in range(1, 31, 2):
    if flag:
        serie += math.pow(Rad, i) / math.factorial(i)
        flag = False
    else:
        serie -= math.pow(Rad, i) / math.factorial(i)
        flag = True
    print("Serie de sen(", ang, ") = ", serie)
    print("===============================================================")
#Coseno
flag_2 = True
serie_2 = 0
for i in range(0, 32, 2):
    if flag_2:
        serie_2 += math.pow(Rad, i) / math.factorial(i)
        flag_2 = False
    else:
        serie_2 -= math.pow(Rad, i) / math.factorial(i)
        flag_2 = True
    print("Serie de cos(", ang, ") = ", serie)
    print("===============================================================")