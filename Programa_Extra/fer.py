import os 
os.system("cls")

# Estudio importante para no ir a repite 

# si es par o impar 
"""n=int(input("Ingresa un numero:"))
if n % 2==0:
    print("Es numero par")
else:
    print("Es numero impar")"""

# Si eres mayor de edad
#n=int(input("Ingresa tu edad: "))
# Si eres mayor de edad
#n=int(input("Ingresa tu edad: "))
#if n >= 18:
#    print("Eres mayor de edad")
#else:
#    print("Eres menor de edad") 

# ------------------------------------------------------------------------

#"""========= MENU PRINCIPAL =========
#1. Calcular área de un rectángulo # A= b x h
#2. Salir
#
#Seleccione una opción:
#Si el usuario selecciona la opción 1:
#- Solicitar la base del rectángulo.
#- Solicitar la altura del rectángulo.
#- Calcular el área.
#- Mostrar el resultado.
#
#Si selecciona la opción 2:
#- Mostrar un mensaje de despedida.
#- Terminar el programa.
#"""

#while True:
#    print("""========= MENU PRINCIPAL =========
#1. Calcular área de un rectángulo # A= b x h
#2. Salir)""")
#    op=int(input("Selecciona una opcion:"))
#    if op ==1: # si es opcion 1
#        b=int(input("Ingresa la base del rectangulo:"))
#        a=int(input("Ingresa la altura del rectangulo:"))
#        A= b*a
#        print("Resultado:",A)
#    elif op ==2: # pero si es opcion 2
#        print("Ya esta listo tu resultado")
#        break
#    else: # Si no es op 1 o op 2 entonces es No valida
#        print("!Opcion no Valida!")

#--------------------------------------------------------------------------------------

# Crea una calculadora: (que solicite 2 numeros)
# suma
# resta
# division
# multiplicacion
# salir


#n1=int(input("Ingresa el primer numero:"))
#n2=int(input("Ingresa el segundo numero:"))
#
#while True:
#    print("""========= MENU PRINCIPAL =========
#    --- Calculadora ---
#    1.- Sumar
#    2.- Restar
#    3.- Dividir
#    4.- Multiplicar
#    5.- Salir
#    """)
#    
#    op=int(input("Selecciona una opcion:"))
#    
#    if op==1:
#        suma= n1 + n2
#        print(" = ",suma)
#
#    elif op==2:
#        resta= n1 - n2 
#        print(" = ",resta)
#
#    elif op==3:
#        division= n1 / n2 
#        print(" = ",division)   #  print(f" = {division:.0f}") -> f y :.0f es para no tener decimales 
#
#    elif op==4:
#        multiplicacion= n1 * n2
#        print(" = ",multiplicacion)
#        
#
#    elif op==5:
#        print("!Salir!")
#        break
#    else:
#        print("opcion no valida")

# ----------------------------------------------------------------------------------------------------------------

"""
Realizar un programa que muestre un menú con tres opciones: calcular promedio, salir y una opción no válida. Si el usuario selecciona calcular promedio, el programa deberá pedir tres calificaciones, 
calcular su promedio y mostrar el resultado. También deberá indicar si el alumno aprobó o reprobó, considerando que la calificación mínima aprobatoria es de 70. Si selecciona salir,
el programa deberá mostrar un mensaje de despedida.
"""


#while True:
#    print("""========= MENU PRINCIPAL =========
#    1.- Calcular Promedio
#    2.- Salir """)
#
#    op=int(input("Selecciona una opcion: "))
#
#    if op==1:
#        n1=int(input("Matematicas:"))
#        n2=int(input("Algebra:"))
#        n3=int(input("Fisica:"))
#
#        Promedio= (n1 + n2 + n3) /3
#        print("Tu promedio es: ",Promedio)
#
#        if Promedio >= 70:
#            print("!Aprobaste!")
#        else:
#            print("!Reprobaste!")
#
#    elif op ==2:
#        print("!Salir!")
#        break
#    else:
#        print("!Opcion No valida!")

#-------------------------------------------------------------------------------

""" Haz un banco con 4 opciones: depositar, retirar, ver saldo , salir"""
cuenta = 0
ultimo_deposito =0

while True:
    print("""========= MENU PRINCIPAL =========
    1.-Depositar
    2.-Retirar
    3.-Checar Saldo
    4.-Salir """)

    op=int(input("Selecciona una opcion: "))
# if sirve para comparar 
    if op==1:
        deposito=int(input("Ingresa la cantidad que deseas depositar: ")) 
        # comprar si el retiro es mayor a 0 si es 0 debe de mostrarte que esa cantidad no es valida
        ultimo_deposito = deposito
        cuenta = cuenta +deposito
        print("Te depositaron",cuenta)
    elif op==2:
        retirar=int(input("Ingresa la cantidad que deseas retirar: "))
        if retirar <= cuenta:
            cuenta= cuenta- retirar # Compara si el retiro es menor o igual a la cuenta
        else:
            print("Saldo retirado")
    elif op==3:
        # compara si quieres ver tu ultimo deposito o toda tu cuenta
        opcion=int(input(" Selecciona una opcion: ")) # Tarea hacer otra opcion la cual sea mostrar el ultimo retiro
        if opcion==1:
            print("Ultimo deposito: ",ultimo_deposito)
        else:
            print("Estado de cuenta: ", cuenta)

    elif op==4:
        print("!Salir!")
        break
    else:
        print("!Opcion No valida!")
