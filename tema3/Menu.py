import os
from Examen import Proyecto, Tarea

os.system("cls")

proyec = Proyecto()

while True:
    print("\n========== MENU DEL PROYECTO ==========")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Buscar tarea por nombre")
    print("4. Actividades por persona")
    print("5. Tareas entre fechas")
    print("6. Tareas finalizadas")
    print("7. Tareas pendientes por persona")
    print("8. Calcular tiempo promedio")
    print("9. Calcular costo total")
    print("10. Eliminar primera tarea")
    print("11. Eliminar ultima tarea")
    print("12. Eliminar tarea por posicion")
    print("13. Modificar tarea por posicion")
    print("14. Eliminar tarea por nombre")
    print("15. Salir")

    opcion = int(input("\nSeleccione una opcion: "))

    if opcion == 1:

        nombre = input("Nombre de la tarea: ")
        costo = float(input("Costo: "))
        tiempo = float(input("Tiempo de ejecucion: "))

        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin_estimada = input("Fecha fin estimada (YYYY-MM-DD): ")

        fecha_fin_efectiva = input(
            "Fecha fin efectiva (Enter si esta pendiente): "
        )

        if fecha_fin_efectiva == "":
            fecha_fin_efectiva = None

        persona = input("Persona a cargo: ")

        tarea = Tarea(
            nombre,
            costo,
            tiempo,
            fecha_inicio,
            fecha_fin_estimada,
            fecha_fin_efectiva,
            persona
        )

        proyec.insertar_tarea(tarea)
        print("Tarea agregada exitosamente")

    elif opcion == 2:
        proyec.mostrar_tareas()

    elif opcion == 3:
        nombre = input("Ingrese el nombre de la tarea: ")
        resultado = proyec.buscar_tarea(nombre)
        print(resultado)

    elif opcion == 4:
        persona = input("Ingrese el nombre de la persona: ")
        proyec.actividades_por_persona(persona)

    elif opcion == 5:
        fecha_inicio = input("Fecha inicial (YYYY-MM-DD): ")
        fecha_fin = input("Fecha final (YYYY-MM-DD): ")
        proyec.tareas_entre_fechas(fecha_inicio, fecha_fin)

    elif opcion == 6:
        proyec.tareas_finalizadas()

    # TAREAS PENDIENTES
    elif opcion == 7:

        persona = input("Ingrese el nombre de la persona: ")
        print("Tareas pendientes:", proyec.tareas_pendientes_por_persona(persona))

    elif opcion == 8:
        print("Tiempo promedio:")
        print(proyec.tiempo_promedio_tareas())

    elif opcion == 9:
        print("Costo total del proyecto:")
        print(proyec.costo_total_proyecto())

    elif opcion == 10:
        print(proyec.eliminar_inicio())

    elif opcion == 11:
        print(proyec.eliminar_final())

    elif opcion == 12:
        posicion = int(input("Ingrese la posicion de la tarea: "))
        print(proyec.eliminar_medio(posicion - 1))

    elif opcion == 13:
        posicion = int(input("Ingrese la posicion de la tarea: "))
        nombre = input("Nuevo nombre: ")
        costo = float(input("Nuevo costo: "))
        tiempo = float(input("Nuevo tiempo de ejecucion: "))
        fecha_inicio = input("Nueva fecha de inicio: ")
        fecha_fin_estimada = input("Nueva fecha fin estimada: ")
        fecha_fin_efectiva = input("Nueva fecha fin efectiva (Enter si esta pendiente): ")
        if fecha_fin_efectiva == "":
            fecha_fin_efectiva = None
        persona = input("Nueva persona a cargo: ")
        nueva_tarea = Tarea(
            nombre,
            costo,
            tiempo,
            fecha_inicio,
            fecha_fin_estimada,
            fecha_fin_efectiva,
            persona
        )
        print(proyec.modificar_elemento(posicion - 1, nueva_tarea))

    elif opcion == 14:
        nombre = input("Ingrese el nombre de la tarea que desea eliminar: ")
        tarea = proyec.buscar_tarea(nombre)
        if isinstance(tarea, Tarea):
            print(proyec.eliminar_elemento(tarea))
        else:
            print(tarea)

    elif opcion == 15:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Intente nuevamente.")
