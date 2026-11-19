import os
os.system("cls")

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Tarea:
    def __init__(self, nombre, costo, tiempo_ejecucion,fecha_inicio, fecha_fin_estimada,fecha_fin_efectiva, persona_a_cargo):   
        self.nombre = nombre
        self.costo = costo
        self.tiempo_ejecucion = tiempo_ejecucion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_estimada = fecha_fin_estimada
        self.fecha_fin_efectiva = fecha_fin_efectiva
        self.persona_a_cargo = persona_a_cargo

    def __str__(self):
        return f"""
        Tarea: {self.nombre}
        Costo: {self.costo}
        Tiempo de ejecución: {self.tiempo_ejecucion}
        Fecha de inicio: {self.fecha_inicio}
        Fecha de fin estimada: {self.fecha_fin_estimada}
        Fecha de fin efectiva: {self.fecha_fin_efectiva}
        Persona a cargo: {self.persona_a_cargo}
        """

class Proyecto:
    def __init__(self):
        self.cabeza = None
        self.tam = 0

    def insertar_tarea(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente 
            aux.siguiente = nuevo
        self.tam += 1

    def tiempo_promedio_tareas(self):
        if self.cabeza is None:
            return "No hay tareas en el proyecto"

        total_tiempo = 0
        aux = self.cabeza
        while aux is not None:
            total_tiempo += aux.dato.tiempo_ejecucion
            aux = aux.siguiente
        return total_tiempo / self.tam

    def costo_total_proyecto(self):
        if self.cabeza is None:
            return "No hay tareas en el proyecto"
        total_costo = 0
        aux = self.cabeza
        while aux is not None:
            total_costo += aux.dato.costo
            aux = aux.siguiente
        return total_costo

    def actividades_por_persona(self, persona):
        if self.cabeza is None:
            print("No hay tareas en el proyecto")
            return
        aux = self.cabeza
        encontrado = False
        while aux is not None:
            if aux.dato.persona_a_cargo == persona:
                print(aux.dato)
                encontrado = True
            aux = aux.siguiente
        if not encontrado:
            print("No se encontraron tareas para esa persona")

    def mostrar_tareas_entre_fechas(self, fecha_inicio, fecha_fin):
        if self.cabeza is None:
            print("No hay tareas en el proyecto")
            return
        aux = self.cabeza
        encontrado = False
        while aux is not None:
            if (aux.dato.fecha_inicio <= fecha_fin and
                aux.dato.fecha_fin_estimada >= fecha_inicio):
                print(aux.dato)
                encontrado = True
            aux = aux.siguiente
        if not encontrado:
            print("No hay tareas en ese periodo")

    def mostrar_tareas_finalizadas(self):
        if self.cabeza is None:
            print("No hay tareas en el proyecto")
            return
        aux = self.cabeza
        a_tiempo = 0
        fuera_tiempo = 0
        print("\n--- TAREAS FINALIZADAS A TIEMPO ---")
        while aux is not None:
            if aux.dato.fecha_fin_efectiva is not None:
                if aux.dato.fecha_fin_efectiva <= aux.dato.fecha_fin_estimada:
                    print(aux.dato)
                    a_tiempo += 1
            aux = aux.siguiente
        aux = self.cabeza
        print("\n--- TAREAS FINALIZADAS FUERA DE TIEMPO ---")
        while aux is not None:
            if aux.dato.fecha_fin_efectiva is not None:

                if aux.dato.fecha_fin_efectiva > aux.dato.fecha_fin_estimada:
                    print(aux.dato)
                    fuera_tiempo += 1
            aux = aux.siguiente
        print("Total a tiempo:", a_tiempo)
        print("Total fuera de tiempo:", fuera_tiempo)

    def tareas_pendientes_por_persona(self, persona):
        if self.cabeza is None:
            return "No hay tareas en el proyecto"

        pendientes = 0
        aux = self.cabeza

        while aux is not None:
            if (aux.dato.persona_a_cargo == persona and
                aux.dato.fecha_fin_efectiva is None):

                pendientes += 1

            aux = aux.siguiente

        return pendientes

    def lista_void(self):
        return self.cabeza is None

    def eliminar_inicio(self):
        if self.lista_void():
            return "La lista esta vacia"

        self.cabeza = self.cabeza.siguiente
        self.tam -= 1

    def eliminar_final(self):
        if self.lista_void():
            return "La lista esta vacia"

        aux = self.cabeza

        if aux.siguiente is None:
            self.cabeza = None
        else:
            while aux.siguiente.siguiente is not None:
                aux = aux.siguiente

            aux.siguiente = None

        self.tam -= 1

    def eliminar_medio(self, posicion):
        if self.lista_void():
            return "La lista esta vacia" 

        if posicion < 0 or posicion >= self.tam:
            return "Posicion fuera de rango"

        if posicion == 0:
            self.eliminar_inicio()
        else:
            aux = self.cabeza

            for _ in range(posicion - 1):
                aux = aux.siguiente

            aux.siguiente = aux.siguiente.siguiente
            self.tam -= 1

    def modificar_elemento(self, posicion, nuevo_dato):
        if self.lista_void():
            return "La lista esta vacia"

        if posicion < 0 or posicion >= self.tam:
            return "Posicion fuera de rango"

        aux = self.cabeza

        for _ in range(posicion):
            aux = aux.siguiente

        aux.dato = nuevo_dato

    def eliminar_elemento(self, dato):
        if self.lista_void():
            return "La lista esta vacia"

        aux = self.cabeza
        prev = None

        while aux is not None:
            if aux.dato == dato:

                if prev is None:
                    self.cabeza = aux.siguiente
                else:
                    prev.siguiente = aux.siguiente

                self.tam -= 1
                return "Tarea eliminada"

            prev = aux
            aux = aux.siguiente

        return "Tarea no encontrada"

    def mostrar_tareas(self):
        if self.lista_void():
            print("La lista esta vacia")
            return

        aux = self.cabeza

        while aux is not None:
            print(aux.dato)
            aux = aux.siguiente

    def buscar_tarea(self, nombre):
        if self.lista_void():
            return "La lista esta vacia"
        aux = self.cabeza
        while aux is not None:
            if aux.dato.nombre == nombre:
                return aux.dato
            aux = aux.siguiente
        return "Tarea no encontrada"

    def buscar_tareas_por_persona(self, persona):
        self.actividades_por_persona(persona)

proyec = Proyecto()
tarea1 = Tarea("Tarea 1", 100, 5, "2024-01-01","2024-01-10", "2024-01-09", "Juan")
nodo1 = Nodo(tarea1)
proyec.insertar_tarea(nodo1)

tarea2 = Tarea("Tarea 2", 200, 10, "2024-01-05","2024-01-15", "2024-01-16", "Maria")
nodo2 = Nodo(tarea2)
proyec.insertar_tarea(nodo2)

tarea3 = Tarea("Tarea 3", 150, 7, "2024-01-10","2024-01-20", "2024-01-19", "Juan")
nodo3 = Nodo(tarea3)
proyec.insertar_tarea(nodo3)

tarea4 = Tarea("Tarea 4", 300, 12, "2024-01-15","2024-01-25", "2024-01-24", "Carlos")
nodo4 = Nodo(tarea4)
proyec.insertar_tarea(nodo4)

tarea5 = Tarea("Tarea 5", 250, 8, "2024-01-20","2024-01-30", "2024-01-29", "Maria")
nodo5 = Nodo(tarea5)
proyec.insertar_tarea(nodo5)

print("\n========== PROYECTO ==========")

print("Tiempo promedio:")
print(proyec.tiempo_promedio_tareas())

print("Costo total:")
print(proyec.costo_total_proyecto())

print("Actividades de Juan:")
proyec.actividades_por_persona("Juan")

print("Tareas entre fechas:")
proyec.mostrar_tareas_entre_fechas("2024-01-05", "2024-01-20")

print("Tareas finalizadas:")
proyec.mostrar_tareas_finalizadas()

print("Tareas pendientes de Juan:")
print(proyec.tareas_pendientes_por_persona("Juan"))

print("========== TODAS LAS TAREAS ==========")
proyec.mostrar_tareas()
print("========== TAREAS DESPUES DE ELIMINAR ==========")
proyec.eliminar_elemento(tarea3)
proyec.mostrar_tareas()