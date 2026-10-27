import os
from  Stack import Stack
os.system("cls")
class EditorTexto:

    def __init__(self):
        
        self.texto = ""
        # Pilas para deshacer y rehacer
        self.pila_deshacer = Stack()
        self.pila_rehacer = Stack()

    def agregar_texto(self, palabra):       
        self.pila_deshacer.apilar(self.texto)    
        self.texto += palabra
        self.pila_rehacer.limpiar()
        print("Texto agregado correctamente.")

    def deshacer(self):
        # Verificar si hay acciones para deshacer
        if self.pila_deshacer.pila_vacia():
            print("No hay acciones para deshacer.")
            return

        # Guardar el texto actual para poder rehacerlo
        self.pila_rehacer.apilar(self.texto)

        # Recuperar el estado anterior
        self.texto = self.pila_deshacer.desapilar()

        print("Acción deshecha correctamente.")

    def rehacer(self):
        # Verificar si hay acciones para rehacer
        if self.pila_rehacer.pila_vacia():
            print("No hay acciones para rehacer.")
            return

        # Guardar el estado actual en la pila de deshacer
        self.pila_deshacer.apilar(self.texto)

        # Recuperar el estado que se había deshecho
        self.texto = self.pila_rehacer.desapilar()

        print("Acción rehecha correctamente.")

    def mostrar_texto(self):
        print("\n--- CONTENIDO DEL EDITOR ---")
        print(self.texto if self.texto else "(El editor está vacío)")
        print("----------------------------")

    def ejecutar(self):
        while True:
            print("\n===== EDITOR DE TEXTO =====")
            print("1. Agregar texto")
            print("2. Deshacer")
            print("3. Rehacer")
            print("4. Mostrar texto")
            print("5. Mostrar pila de deshacer")
            print("6. Mostrar pila de rehacer")
            print("7. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                palabra = input("Escribe el texto que deseas agregar: ")
                self.agregar_texto(palabra)

            elif opcion == "2":
                self.deshacer()

            elif opcion == "3":
                self.rehacer()

            elif opcion == "4":
                self.mostrar_texto()

            elif opcion == "5":
                print("\nPila de deshacer:")
                self.pila_deshacer.mostrar_elementos()

            elif opcion == "6":
                print("\nPila de rehacer:")
                self.pila_rehacer.mostrar_elementos()

            elif opcion == "7":
                print("Cerrando el editor de texto...")
                break

            else:
                print("Opción no válida. Intenta nuevamente.")


# Programa principal
if __name__ == "__main__":
    editor = EditorTexto()
    editor.ejecutar()

