import os 
os.system("cls")

demanda = [1, 3, 2, 4]
produccion = [0, 0, 0, 0]

costo_total = 0
inventario = 0

for i in range(4):

    print("\nMes", i + 1)
    produccion[i] = demanda[i] - inventario

    if produccion[i] < 0:
        produccion[i] = 0
    if produccion[i] > 0:
        costo_total += 3 + produccion[i]

    inventario += produccion[i] - demanda[i]
    costo_total += inventario * 0.5
    print("Demanda:", demanda[i])
    print("Produccion:", produccion[i])
    print("Inventario:", inventario)

print("\nCosto total:", costo_total)
