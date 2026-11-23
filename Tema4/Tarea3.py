import os
import networkx as nx
import matplotlib.pyplot as plt
import csv
os.system("cls")

G = nx.DiGraph()
def agregar_dioses():
    dioses = {
        "Cronos": "Titan asociado al tiempo.",
        "Rea": "Titanide madre de los dioses olimpicos.",
        "Zeus": "Dios del cielo y gobernante del Olimpo.",
        "Poseidon": "Dios del mar.",
        "Hades": "Dios del inframundo.",
        "Hera": "Diosa del matrimonio y la familia.",
        "Demeter": "Diosa de la agricultura.",
        "Hestia": "Diosa del hogar.",
        "Persefone": "Diosa de la primavera y el inframundo.",
        "Ares": "Dios de la guerra.",
        "Hefesto": "Dios del fuego y la metalurgia.",
        "Atenea": "Diosa de la sabiduria.",
        "Apolo": "Dios de la musica y las artes.",
        "Artemisa": "Diosa de la caza.",
        "Dionisio": "Dios del vino.",
        "Hermes": "Dios mensajero.",
        "Tea": "Titanide asociada a la luz.",
        "Hiperion": "Titan asociado a la luz celestial.",
        "Helios": "Dios del Sol.",
        "Selene": "Diosa de la Luna.",
        "Eos": "Diosa del amanecer.",
        "Metis": "Titanide asociada a la prudencia.",
        "Leto": "Titanide madre de Apolo y Artemisa.",
        "Semele": "Madre mortal de Dionisio.",
        "Maia": "Madre de Hermes."
    }
    for dios, descripcion in dioses.items():
        G.add_node(dios, descripcion=descripcion)

def agregar_relacion(origen, destino, relacion):
    G.add_edge(origen, destino, relacion=relacion)
    if relacion in ["padre", "madre"]:
        G.add_edge(destino, origen, relacion="hijo")
    elif relacion in ["hermano", "pareja"]:
        G.add_edge(destino, origen, relacion=relacion)


def cargar_relaciones():
    # Hijos de Cronos y Rea
    hijos_cronos = [
        "Zeus", "Poseidon", "Hades",
        "Hera", "Demeter", "Hestia"
    ]
    agregar_relacion("Cronos", "Rea", "pareja")

    for hijo in hijos_cronos:
        agregar_relacion("Cronos", hijo, "padre")
        agregar_relacion("Rea", hijo, "madre")
    # Hijos de Zeus
    agregar_relacion("Zeus", "Hera", "pareja")
    # Atenea
    agregar_relacion("Zeus", "Metis", "pareja")
    agregar_relacion("Zeus", "Atenea", "padre")
    agregar_relacion("Metis", "Atenea", "madre")
    # Apolo y Artemisa
    agregar_relacion("Zeus", "Leto", "pareja")

    for hijo in ["Apolo", "Artemisa"]:
        agregar_relacion("Zeus", hijo, "padre")
        agregar_relacion("Leto", hijo, "madre")
    # Dionisio
    agregar_relacion("Zeus", "Semele", "pareja")
    agregar_relacion("Zeus", "Dionisio", "padre")
    agregar_relacion("Semele", "Dionisio", "madre")
    # Hermes
    agregar_relacion("Zeus", "Maia", "pareja")
    agregar_relacion("Zeus", "Hermes", "padre")
    agregar_relacion("Maia", "Hermes", "madre")

    for hijo in ["Ares", "Hefesto"]:
        agregar_relacion("Zeus", hijo, "padre")
        agregar_relacion("Hera", hijo, "madre")

    # Persefone
    agregar_relacion("Zeus", "Persefone", "padre")
    agregar_relacion("Demeter", "Persefone", "madre")
    agregar_relacion("Tea", "Hiperion", "pareja")
    hijos_tea = ["Helios", "Selene", "Eos"]
    for hijo in hijos_tea:
        agregar_relacion("Hiperion", hijo, "padre")
        agregar_relacion("Tea", hijo, "madre")
    for padre, hijo1, datos in list(G.edges(data=True)):
        if datos["relacion"] in ["padre", "madre"]:
            hermanos = [
                destino
                for origen, destino, relacion in G.edges(data=True)
                if origen == padre
                and relacion["relacion"] in ["padre", "madre"]
            ]
            for hijo2 in hermanos:
                if hijo1 != hijo2:
                    if not G.has_edge(hijo1, hijo2):
                        agregar_relacion(hijo1, hijo2, "hermano")

def mostrar_hijos(dios):
    dios = dios.strip().title()
    if dios not in G:
        print("El dios no existe.")
        return
    print("\nHijos de:", dios)
    encontrados = False
    for origen, destino, datos in G.out_edges(dios, data=True):
        if datos["relacion"] in ["padre", "madre"]:
            print("-", destino)
            encontrados = True
    if not encontrados:
        print("No tiene hijos registrados.")

def informacion_dios(dios):
    dios = dios.strip().title()
    if dios not in G:
        print("El dios no existe.")
        return
    print("\n========== INFORMACION ==========")
    print("Nombre:", dios)
    print("Descripcion:", G.nodes[dios]["descripcion"])
    print("\nPadres:")
    for origen, destino, datos in G.in_edges(dios, data=True):
        if datos["relacion"] in ["padre", "madre"]:
            print(datos["relacion"].title() + ":", origen)
    print("\nHermanos:")
    hermanos = [
        destino
        for origen, destino, datos in G.out_edges(dios, data=True)
        if datos["relacion"] == "hermano"
    ]
    print(hermanos if hermanos else "No tiene hermanos registrados.")
    print("\nHijos:")
    hijos = [
        destino
        for origen, destino, datos in G.out_edges(dios, data=True)
        if datos["relacion"] in ["padre", "madre"]
    ]
    print(hijos if hijos else "No tiene hijos registrados.")

def relacion_directa():
    dios1 = input("\nPrimer dios: ").strip().title()
    dios2 = input("Segundo dios: ").strip().title()
    if dios1 not in G or dios2 not in G:
        print("Uno de los dioses no existe.")
        return
    if G.has_edge(dios1, dios2):
        datos = G.get_edge_data(dios1, dios2)
        print("\nExiste una relacion directa:")
        for dato in datos.values():
            print(dios1, "->", dios2, ":", dato["relacion"])
    else:
        print("No existe una relacion directa entre ellos.")

def camino_corto():
    inicio = input("\nDios de origen: ").strip().title()
    final = input("Dios de destino: ").strip().title()
    try:
        ruta = nx.shortest_path(
            G,
            source=inicio,
            target=final
        )
        print("\nCamino mas corto:")
        print(" -> ".join(ruta))
        print("Cantidad de aristas:", len(ruta) - 1)
    except nx.NodeNotFound:
        print("Error: El dios no existe.")

    except nx.NetworkXNoPath:
        print("No existe un camino entre los dioses.")

def recorridos():
    inicio = input("\nDios inicial: ").strip().title()
    if inicio not in G:
        print("El dios no existe.")
        return

    profundidad = list(
        nx.dfs_preorder_nodes(G, source=inicio)
    )

    amplitud = list(
        nx.bfs_tree(G, source=inicio).nodes()
    )

    print("\nRecorrido en profundidad (DFS):")
    print(" -> ".join(profundidad))
    print("\nRecorrido en amplitud (BFS):")
    print(" -> ".join(amplitud))

def mostrar_madres():
    print("\n========== DIOSES Y SUS MADRES ==========")
    for dios in G.nodes():
        madre = []
        for origen, destino, datos in G.in_edges(dios, data=True):
            if datos["relacion"] == "madre":
                madre.append(origen)
        print(dios, "- Madre:", ", ".join(madre) if madre else "Desconocida")

def mostrar_ancestros():
    dios = input("\nNombre del dios: ").strip().title()
    if dios not in G:
        print("El dios no existe.")
        return
    
    visitados = set()
    pila = [dios]
    ancestros = []

    while pila:
        actual = pila.pop()
        for origen, destino, datos in G.in_edges(actual, data=True):
            if datos["relacion"] in ["padre", "madre"]:
                if origen not in visitados:
                    visitados.add(origen)
                    ancestros.append(origen)
                    pila.append(origen)
    print("\nAncestros de", dios, ":")

    if ancestros:
        print(" -> ".join(ancestros))
    else:
        print("No tiene ancestros registrados.")

def nietos_cronos():
    nietos = set()

    for hijo in G.successors("Cronos"):
        if G["Cronos"][hijo]["relacion"] == "padre":
            for nieto in G.successors(hijo):
                if G[hijo][nieto]["relacion"] in ["padre", "madre"]:
                    nietos.add(nieto)
    print("\nNietos de Cronos:")

    if nietos:
        print(", ".join(sorted(nietos)))
    else:
        print("No hay nietos registrados.")

def hijos_tea():
    mostrar_hijos("Tea")

def guardar_archivos():

    with open("vertices.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Dios", "Descripcion"])

        for dios, datos in G.nodes(data=True):
            escritor.writerow([
                dios,
                datos["descripcion"]
            ])
    with open("aristas.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Origen", "Destino", "Relacion"])
        for origen, destino, datos in G.edges(data=True):
            escritor.writerow([
                origen,
                destino,
                datos["relacion"]
            ])

    print("\nArchivos guardados correctamente.")
    print("vertices.csv")
    print("aristas.csv")

def dibujar():
    posiciones = nx.spring_layout(G, seed=42, k=1.5)
    plt.figure(figsize=(17, 12))
    nx.draw_networkx_nodes(
        G, posiciones,
        node_color="lightblue",
        node_size=1600,
        edgecolors="black"
    )

    nx.draw_networkx_labels(
        G, posiciones,
        font_size=9,
        font_weight="bold"
    )

    padres = []
    hermanos = []
    parejas = []
    etiquetas = {}

    for origen, destino, datos in G.edges(data=True):
        relacion = datos["relacion"]
        if relacion in ["padre", "madre"]:
            padres.append((origen, destino))
            etiquetas[(origen, destino)] = relacion
        elif relacion == "hermano" and origen < destino:
            hermanos.append((origen, destino))
            etiquetas[(origen, destino)] = relacion
        elif relacion == "pareja" and origen < destino:
            parejas.append((origen, destino))
            etiquetas[(origen, destino)] = relacion

    nx.draw_networkx_edges(
        G, posiciones,
        edgelist=padres,
        arrows=True,
        arrowsize=15,
        edge_color="black"
    )

    nx.draw_networkx_edges(
        G, posiciones,
        edgelist=hermanos,
        arrows=False,
        edge_color="gray",
        width=1.5
    )

    nx.draw_networkx_edges(
        G, posiciones,
        edgelist=parejas,
        arrows=False,
        edge_color="red",
        style="dashed",
        width=2
    )

    nx.draw_networkx_edge_labels(
        G, posiciones,
        edge_labels=etiquetas,
        font_size=7,
        rotate=False
    )

    plt.title("Arbol genealogico de los dioses griegos")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# ==========================================
# MENU PRINCIPAL
# ==========================================

agregar_dioses()
cargar_relaciones()

while True:
    print("""\n========== MENU PRINCIPAL ==========
    (1. Mostrar hijos de un dios")
    (2. Informacion completa de un dios")
    (3. Buscar relacion directa")
    (4. Camino mas corto")
    (5. Recorridos DFS y BFS")
    (6. Mostrar dioses y sus madres")
    (7. Mostrar ancestros")
    (8. Mostrar nietos de Cronos")
    (9. Mostrar hijos de Tea")
    (10. Guardar vertices y aristas")
    (11. Dibujar grafo")
    (12. Mostrar todas las conexiones")
    (0. Salir")""")

    opcion = input("\nSelecciona una opcion: ")
    if opcion == "1":
        dios = input("Nombre del dios: ")
        mostrar_hijos(dios)
    elif opcion == "2":
        dios = input("Nombre del dios: ")
        informacion_dios(dios)
    elif opcion == "3":
        relacion_directa()
    elif opcion == "4":
        camino_corto()
    elif opcion == "5":
        recorridos()
    elif opcion == "6":
        mostrar_madres()
    elif opcion == "7":
        mostrar_ancestros()
    elif opcion == "8":
        nietos_cronos()
    elif opcion == "9":
        hijos_tea()
    elif opcion == "10":
        guardar_archivos()
    elif opcion == "11":
        dibujar()
    elif opcion == "12":
        for origen, destino, datos in G.edges(data=True):
            print(
                origen, "->", destino,
                "Relacion:", datos["relacion"]
            )
    elif opcion == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opcion no valida.")
