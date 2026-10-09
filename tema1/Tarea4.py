
import os
import numpy as np

os.system("cls")

# Calificaciones de 30 alumnos en 6 materias
calificaciones = np.random.randint(0, 101, (30, 6))


class Promedios:
    def __init__(self, calificaciones):
        self.cali = calificaciones
        self.materias = [
            "Calculo Vectorial",
            "Estructura de datos",
            "Fisica",
            "Metodos",
            "Cultura Empresarial",
            "Investigacion"
        ]

    def alumno(self):
        self.prom_alumno = np.mean(self.cali, axis=1)
        resultado = []

        for i in range(30):
            resultado.append(
                f"El promedio del alumno {i+1} es de "
                f"{self.prom_alumno[i]:.2f}"
            )

        return "\n".join(resultado)

    def materia(self):
        self.prom_materia = np.mean(self.cali, axis=0)
        prom = []

        for i, materia in enumerate(self.materias):
            prom.append(
                f"El promedio de {materia} es de: "
                f"{self.prom_materia[i]:.2f}"
            )

        return "\n".join(prom)

    def cali_max_o_min(self):
        max_cali = np.max(self.cali, axis=0)
        min_cali = np.min(self.cali, axis=0)
        resultado = []

        for i, materia in enumerate(self.materias):
            resultado.append(
                f"{materia}: calificacion maxima = {max_cali[i]}, "
                f"calificacion minima = {min_cali[i]}"
            )

        return "\n".join(resultado)

    def alumnos_destacados(self):
        promedios = np.mean(self.cali, axis=1)
        resultado = []

        for i in range(30):
            if promedios[i] >= 90:
                resultado.append(
                    f"El alumno {i+1} tiene un promedio de: "
                    f"{promedios[i]:.2f}"
                )

        if len(resultado) == 0:
            return "No hay alumnos con promedio mayor o igual a 90."

        return "\n".join(resultado)

    def materias_reprobadas(self):
        promedios = np.mean(self.cali, axis=0)
        resultado = []

        for i, materia in enumerate(self.materias):
            if promedios[i] < 70:
                resultado.append(
                    f"La materia {materia} tiene un promedio de: "
                    f"{promedios[i]:.2f}"
                )

        if len(resultado) == 0:
            return "No hay materias con promedio menor a 70."

        return "\n".join(resultado)

    def ordenar_alumnos(self):
        promedios = np.mean(self.cali, axis=1)
        indices = np.argsort(promedios)[::-1]
        resultado = []

        for i in indices:
            resultado.append(f"Alumno {i+1}: {promedios[i]:.2f}")

        return "\n".join(resultado)

    def desviacion_estandar(self):
        desviacion = np.std(self.cali, axis=0)
        resultado = []

        for i, materia in enumerate(self.materias):
            resultado.append(f"{materia}: {desviacion[i]:.2f}")

        return "\n".join(resultado)

    def alumnos_reprobados(self):
        cantidad = np.sum(self.cali < 70, axis=0)
        resultado = []

        for i, materia in enumerate(self.materias):
            resultado.append(
                f"{materia}: {cantidad[i]} alumnos reprobados"
            )

        return "\n".join(resultado)

    def reemplazar_menores_60(self):
        self.cali[self.cali < 60] = 0
        return self.cali

    def transpuesta(self):
        return self.cali.T

    def multiplicacion(self):
        return np.matmul(self.cali, self.cali.T)

    def diagonal_traza(self):
        matriz = self.multiplicacion()
        diagonal = np.diag(matriz)
        traza = np.trace(matriz)
        return diagonal, traza

    def reporte_estadistico(self):
        promedio_alumnos = np.mean(self.cali, axis=1)
        promedio_materias = np.mean(self.cali, axis=0)
        maximo = np.max(self.cali, axis=0)
        minimo = np.min(self.cali, axis=0)
        desviacion = np.std(self.cali, axis=0)
        reprobados = np.sum(self.cali < 70, axis=0)

        return (
            "\n========== REPORTE ESTADISTICO ==========\n"
            f"Promedio general: {np.mean(self.cali):.2f}\n"
            f"Calificacion general maxima: {np.max(self.cali)}\n"
            f"Calificacion general minima: {np.min(self.cali)}\n"
            f"Desviacion estandar general: {np.std(self.cali):.2f}\n"
            f"Total de calificaciones: {self.cali.size}\n"
            f"Promedio mas alto de alumno: "
            f"{np.max(promedio_alumnos):.2f}\n"
            f"Promedio mas bajo de alumno: "
            f"{np.min(promedio_alumnos):.2f}\n"
            f"\nPromedios por materia:\n{promedio_materias}\n"
            f"\nMaximas por materia:\n{maximo}\n"
            f"\nMinimas por materia:\n{minimo}\n"
            f"\nDesviacion estandar por materia:\n{desviacion}\n"
            f"\nAlumnos reprobados por materia:\n{reprobados}\n"
        )


promedio = Promedios(calificaciones)

print(promedio.alumno())
print("-" * 55)
print(promedio.materia())
print("-" * 55)
print(promedio.cali_max_o_min())
print("-" * 55)
print(promedio.alumnos_destacados())
print("-" * 55)
print(promedio.materias_reprobadas())
print("-" * 55)
print(promedio.ordenar_alumnos())
print("-" * 55)
print(promedio.desviacion_estandar())
print("-" * 55)
print(promedio.alumnos_reprobados())
print("-" * 55)
print(promedio.reemplazar_menores_60())
print("-" * 55)
print(promedio.transpuesta())
print("-" * 55)
print(promedio.multiplicacion())
print("-" * 55)
print(promedio.diagonal_traza())
print("-" * 55)
print(promedio.reporte_estadistico())
print("-" * 55)