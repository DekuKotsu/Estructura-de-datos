import os
from  Stack import Stack
os.system("cls")
class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.pila_deshacer = []
        self.pila_rehacer = []

    def escribir(self, contenido):
        # Guardar el estado anterior
        self.pila_deshacer.append(self.texto)

        # Una nueva acción invalida el historial de rehacer
        self.pila_rehacer.clear()

        self.texto += contenido
        print("Texto actualizado:", self.texto)

    def deshacer(self):
        if not self.pila_deshacer:
            print("No hay acciones para deshacer.")
            return

        # Guardar el estado actual para poder rehacerlo
        self.pila_rehacer.append(self.texto)

        # Recuperar el último estado anterior
        self.texto = self.pila_deshacer.pop()
        print("Deshacer:", self.texto)

    def rehacer(self):
        if not self.pila_rehacer:
            print("No hay acciones para rehacer.")
            return

        # Guardar el estado actual en la pila de deshacer
        self.pila_deshacer.append(self.texto)

        # Recuperar el último estado deshecho
        self.texto = self.pila_rehacer.pop()
        print("Rehacer:", self.texto)

    def mostrar(self):
        print("Texto actual:", self.texto)


# Programa principal
editor = EditorTexto()

while True:
    print("\n--- EDITOR DE TEXTO ---")
    print("1. Escribir texto")
    print("2. Deshacer")
    print("3. Rehacer")
    print("4. Mostrar texto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        contenido = input("Escribe el texto que deseas agregar: ")
        editor.escribir(contenido)

    elif opcion == "2":
        editor.deshacer()

    elif opcion == "3":
        editor.rehacer()

    elif opcion == "4":
        editor.mostrar()

    elif opcion == "5":
        print("Cerrando editor...")
        break

    else:
        print("Opción no válida.")
#Programa inicial
if __name__ == "__main__":
    editor = EditorTexto()
    editor.ejecutar()