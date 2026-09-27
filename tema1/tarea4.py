#Calificacion de 30 alumnos de 6 materias
import os, random
import numpy as np
os.system("cls")
calificaciones = np.random.randint(0,101, (30,6))
class promedios:
    def __init__(self, calificaciones):
        self.prom_alumno = 0
        self.prom_materia = 0
        self.cali = calificaciones
        self.materias = [
            "calculo Vectorial",
            "Estructura de datos",
            "Física",
            "metodos",
            "Cultura Empresarial",
            "Investigación"
        ]
    def alumno (self):
        self.prom_alumno = np.mean(self.cali, axis=1)
        resultado = []
        for i in range(30):
            resultado.append(f"El promedio del alumno {i+1} es de, {self.prom_alumno[i]:.2f} " )
        return "\n" .join(resultado)

    def materia(self):
        self.prom_materia = np.mean(self.cali, axis=0)
        prom = []
        for i,materia in enumerate(self.materias):
            prom.append(f"El promedio de la materia {materia} es de: {self.prom_materia[i]:.2f}")
        return "\n" .join(prom)
    
promedio =promedios(calificaciones)
print(promedio.alumno())
print("-"*55)
print(promedio.materia())
print("-"*55)