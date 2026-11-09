import os 
from Examen import Proyecto, Tarea
os.system("cls")
proyec = Proyecto()

while True:
    print("\n========== MENU ==========")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Actividades por persona")
    print("4. Tareas entre fechas")
    print("5. Tareas finalizadas")
    print("6. Tareas pendientes por persona")
    print("7.-salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre de la tarea: ")
        costo = float(input("Ingrese el costo de la tarea: "))
        tiempo_ejecucion = float(input("Ingrese el tiempo de ejecución: "))
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin_estimada = input("Ingrese la fecha de fin estimada (YYYY-MM-DD): ")
        fecha_fin_efectiva = input("Ingrese la fecha de fin efectiva (YYYY-MM-DD): ")
        persona_a_cargo = input("Ingrese la persona a cargo: ")

        tarea = Tarea(nombre, costo, tiempo_ejecucion,fecha_inicio, fecha_fin_estimada,fecha_fin_efectiva, persona_a_cargo)

        proyec.insertar_tarea(tarea)
        print("Tarea agregada exitosamente.")

    elif opcion == 2:
        proyec.mostrar_tareas()
    
    elif opcion == 3:
        persona = input("Ingrese el nombre de la persona: ")
        proyec.actividades_por_persona(persona)
    
    elif opcion == 4:
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        proyec.tareas_entre_fechas(fecha_inicio, fecha_fin)
    
    elif opcion == 5:
        proyec.tareas_finalizadas()
    
    elif opcion == 6:
        persona = input("Ingrese el nombre de la persona: ")
        proyec.tareas_pendientes_por_persona(persona)
    elif opcion == 7:
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")