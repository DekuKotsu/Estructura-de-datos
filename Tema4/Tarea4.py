import os
import networkx as nx
import matplotlib.pyplot as plt
os.system("cls")

G = nx.Graph()

G.add_node("Mendoza",
    codigo="MZA-123",
    latitud=-32.89,
    longitud=-68.84,
    velocidad=100
)

G.add_node("SanLuis",
    codigo="SLU-456",
    latitud=-33.30,
    longitud=-66.33,
    velocidad=80
)

G.add_node("Cordoba",
    codigo="COR-789",
    latitud=-31.42,
    longitud=-64.18,
    velocidad=120
)

G.add_node("SantaFe",
    codigo="SFE-321",
    latitud=-31.63,
    longitud=-60.70,
    velocidad=90
)

G.add_node("Misiones",
    codigo="MIS-654",
    latitud=-27.36,
    longitud=-55.90,
    velocidad=110
)

G.add_node("BuenosAires",
    codigo="BUE-987",
    latitud=-34.60,
    longitud=-58.38,
    velocidad=150
)

G.add_node("AntenaTGK",
    codigo="TGK-783",
    latitud=-30.00,
    longitud=-60.00,
    velocidad=75
)

G.add_weighted_edges_from(
    [
        ("Mendoza", "SanLuis", 250),
        ("Mendoza", "Cordoba", 450),
        ("SanLuis", "Cordoba", 180),
        ("Cordoba", "SantaFe", 350),
        ("SantaFe", "Misiones", 700),
        ("Cordoba", "Misiones", 900),
        ("BuenosAires", "SantaFe", 400),
        ("BuenosAires", "Misiones", 1000),
        ("SantaFe", "AntenaTGK", 200),
        ("AntenaTGK", "Misiones", 600)
    ],
    weight="distancia"
)

print("========== CONEXIONES DEL GRAFO ==========")
for origen, destino, datos in G.edges(data=True):
    print(
        origen, "-", destino,
        "Distancia:", datos["distancia"], "Km"
    )

def tamanio_grafo():
    print("\n========== TAMAÑO DEL GRAFO ==========")
    print("Cantidad de vertices:", G.number_of_nodes())
    print("Cantidad de aristas:", G.number_of_edges())

def camino_corto():
    inicio = "Mendoza"
    final = "Misiones"
    try:
        ruta = nx.dijkstra_path(
            G,
            source=inicio,
            target=final,
            weight="distancia"
        )
        distancia = nx.dijkstra_path_length(
            G,
            source=inicio,
            target=final,
            weight="distancia"
        )
        print("\n========== RESULTADO DIJKSTRA ==========")
        print("Ruta mas corta:", " -> ".join(ruta))
        print("Distancia total:", distancia, "Km")

        posiciones = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(10, 7))

        nx.draw_networkx_nodes(
            G, posiciones,
            node_color="lightblue",
            node_size=1800
        )

        nx.draw_networkx_edges(
            G, posiciones,
            edge_color="gray",
            width=2
        )

        nx.draw_networkx_labels(
            G, posiciones,
            font_size=10,
            font_weight="bold"
        )

        etiquetas = nx.get_edge_attributes(G, "distancia")

        nx.draw_networkx_edge_labels(
            G, posiciones,
            edge_labels=etiquetas
        )

        arista_ruta = list(zip(ruta, ruta[1:]))
        nx.draw_networkx_edges(
            G, posiciones,
            edgelist=arista_ruta,
            edge_color="red",
            width=4
        )
        plt.title("Camino mas corto: Mendoza a Misiones")
        plt.axis("off")
        plt.show()
    except nx.NodeNotFound:
        print("Error: La antena no existe.")
    except nx.NetworkXNoPath:
        print("No existe una ruta entre las antenas.")

def arbol_minimo():
    arbol = nx.minimum_spanning_tree(
        G,
        algorithm="prim",
        weight="distancia"
    )
    print("\n========== ARBOL DE EXPANSION MINIMA ==========")
    for origen, destino, datos in arbol.edges(data=True):
        print(
            origen, "-", destino,
            "Distancia:", datos["distancia"], "Km"
        )
    total = arbol.size(weight="distancia")
    print("\nDistancia total:", total, "Km")
    posiciones = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(
        G, posiciones,
        node_color="lightblue",
        node_size=1800
    )

    nx.draw_networkx_edges(
        G, posiciones,
        edge_color="gray",
        width=1.5
    )

    nx.draw_networkx_edges(
        arbol, posiciones,
        edge_color="green",
        width=4
    )

    nx.draw_networkx_labels(
        G, posiciones,
        font_size=10,
        font_weight="bold"
    )
    etiquetas = nx.get_edge_attributes(G, "distancia")

    nx.draw_networkx_edge_labels(
        G, posiciones,
        edge_labels=etiquetas
    )
    plt.title("Arbol de expansion minima - Prim")
    plt.axis("off")
    plt.show()

def buscar_antena():
    codigo = input("\nIngrese el codigo de la antena: ").upper()
    encontrada = False
    for antena, datos in G.nodes(data=True):
        if datos["codigo"] == codigo:
            print("\n========== ANTENA ENCONTRADA ==========")
            print("Nombre:", antena)
            print("Codigo:", datos["codigo"])
            print("Latitud:", datos["latitud"])
            print("Longitud:", datos["longitud"])
            print("Velocidad:", datos["velocidad"], "MB/s")
            print("\nAntenas conectadas:")

            for vecino in G.neighbors(antena):
                print(
                    vecino,
                    "Distancia:",
                    G[antena][vecino]["distancia"],
                    "Km"
                )
            encontrada = True
            break
    if not encontrada:
        print("La antena no existe.")

def dibujar_grafo():
    posiciones = {
        "BuenosAires": (-4, 2),
        "Misiones": (-2, 3),
        "SantaFe": (-2, 0),
        "AntenaTGK": (-4, -2),
        "Cordoba": (1, 0),
        "Mendoza": (3, 3),
        "SanLuis": (4, 0)
    }

    plt.figure(figsize=(13, 8))
    nx.draw_networkx_nodes(
        G, posiciones,
        node_color="lightblue",
        node_size=2200,
        edgecolors="black"
    )
    nx.draw_networkx_edges(
        G, posiciones,
        edge_color="gray",
        width=2
    )

    nx.draw_networkx_labels(
        G, posiciones,
        font_size=10,
        font_weight="bold"
    )

    etiquetas = nx.get_edge_attributes(
        G, "distancia"
    )
    nx.draw_networkx_edge_labels(
        G, posiciones,
        edge_labels=etiquetas,
        font_size=9,
        rotate=False,
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.8
        )
    )

    plt.title("Red de antenas telefonicas", fontsize=15)

    plt.axis("off")
    plt.tight_layout()
    plt.show()


while True:
    print("""\n========== MENU PRINCIPAL ==========)
    1. Mostrar tamaño del grafo
    2. Camino mas corto (Dijkstra)
    3. Arbol de expansion minima (Prim)
    4. Buscar antena TGK-783
    5. visulizar grafo
    0. Salir""")
    opcion = input("\nSelecciona una opcion: ")
    if opcion == "1":
        tamanio_grafo()
    elif opcion == "2":
        camino_corto()
    elif opcion == "3":
        arbol_minimo()
    elif opcion == "4":
        buscar_antena()
    elif opcion =="5":
        dibujar_grafo()
    elif opcion == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opcion incorrecta.")