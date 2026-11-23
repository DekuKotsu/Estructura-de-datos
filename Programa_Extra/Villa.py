
import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")

def funcion_objetivo(x, y):
    return (x - 3)**2 + (y - 2)**2

def metodo_directo():

    mejor_x = 0
    mejor_y = 0
    mejor_z = funcion_objetivo(mejor_x, mejor_y)

    paso = 0.1
    radio = 3

    while paso >= 0.00001:

        inicio_x = max(0, mejor_x - radio)
        final_x = min(3, mejor_x + radio)

        inicio_y = max(0, mejor_y - radio)
        final_y = min(3, mejor_y + radio)

        valores_x = np.arange(
            inicio_x, final_x + paso / 2, paso
        )

        valores_y = np.arange(
            inicio_y, final_y + paso / 2, paso
        )

        X, Y = np.meshgrid(valores_x, valores_y)

        Z = funcion_objetivo(X, Y)

        factible = (X >= 0) & (Y >= 0) & (X + Y <= 3)

        Z = np.where(factible, Z, np.inf)

        indice = np.argmin(Z)

        fila, columna = np.unravel_index(indice, Z.shape)

        if Z[fila, columna] < mejor_z:
            mejor_x = X[fila, columna]
            mejor_y = Y[fila, columna]
            mejor_z = Z[fila, columna]

        radio = paso
        paso = paso / 10

    print("RESULTADOS DEL METODO DIRECTO")
    print("--------------------------------")
    print("Valor de X:", round(mejor_x, 5))
    print("Valor de Y:", round(mejor_y, 5))
    print("Valor minimo de Z:", round(mejor_z, 8))

    print("--------------------------------")
    print("VERIFICACION DE RESTRICCIONES")
    print("X + Y =", round(mejor_x + mejor_y, 5))
    print("X >= 0:", mejor_x >= 0)
    print("Y >= 0:", mejor_y >= 0)
    print("--------------------------------")
    valores_x = np.linspace(0, 3, 200)
    valores_y = np.linspace(0, 3, 200)

    X, Y = np.meshgrid(valores_x, valores_y)

    Z = funcion_objetivo(X, Y)

    factible = X + Y <= 3

    Z = np.where(factible, Z, np.nan)

    plt.figure(figsize=(9, 7))

    grafica = plt.contourf(
        X, Y, Z,
        levels=25,
        cmap="viridis"
    )

    plt.colorbar(grafica, label="Valor de Z")

    plt.contour(
        X, Y, Z,
        levels=10,
        colors="black",
        alpha=0.5
    )

    plt.plot(
        [0, 3], [3, 0],
        color="red",
        label="x + y = 3"
    )

    plt.fill(
        [0, 3, 0],
        [0, 0, 3],
        alpha=0.15,
        color="cyan",
        label="Region factible"
    )

    plt.scatter(
        mejor_x, mejor_y,
        color="red",
        s=100,
        label="Punto optimo"
    )

    plt.annotate(
        f"({mejor_x:.2f}, {mejor_y:.2f})",
        (mejor_x, mejor_y),
        xytext=(10, 10),
        textcoords="offset points"
    )

    plt.title("Metodo directo de programacion no lineal")
    plt.xlabel("Variable X")
    plt.ylabel("Variable Y")

    plt.xlim(0, 3)
    plt.ylim(0, 3)

    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()


metodo_directo()
