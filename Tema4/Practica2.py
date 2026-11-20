#Grafos
import os 
import networkx as nx
import matplotlib.pyplot as plt
os.system("cls")
G = nx.Graph()

G.add_weighted_edges_from(
    [
    ("A", "B", 4),
    ("A", "C", 3),
    ("B", "C", 2),
    ("B", "D", 5),
    ("C", "D", 3),
    ("C", "E", 6),
    ("D", "E", 2),
    ("D", "F", 4),
    ("E", "F", 3),
    ("E", "G", 5),
    ("F", "H", 2),
    ("G", "H", 3)
    ]
)
print("CONEXIONES DE GRAFO")
for origen, destino, datos in G.edges(data=True):
    print(origen, "-", destino,
        "Distacia:", datos["weight"], "Km")

incio = input("\nCiudad de Origen (A-H): ").upper()
final = input("Ciudad de destino (A-H): ").upper()
try:
    ruta = nx.dijkstra_path(
        G,
        source= incio,
        target= final,
        weight= "weight"
    )
    distancia = nx.dijkstra_path_length(
        G,
        source= incio,
        target= final,
        weight="weight"
    )
    print("\nResultado de dijkstra")
    print("Ruta mas corta: ", "->".join(ruta))
    print("Distancia total:", distancia, "Km")

    posiciones= nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10,7))
    nx.draw_networkx_nodes(
        G, posiciones,
        node_color= "lighblue",
        node_size=1800
    )
    #aristas
    nx.draw_networkx_edge(
        G, posiciones,
        edge_color = "gray",
        width = 2
    )
    #etiquetas
    nx.draw_networkx_labels(
        G, posiciones,
        font_size= 12,
        font_weight= "bold"
    )
    #etiquetas de las distancias
    etiqueta = nx.get_edge_attributes(
        G, "weight"
    )
    arista_ruta = list(zip(ruta, ruta[1:]))

    nx.draw_networkx_edge(
        G, posiciones,
        edgelist = arista_ruta,
        edge_color= "red",
        width = 4
    )

    plt.title(
        f"Ruta mas corta: {incio} a {final}"
    )
    plt.axis("off")
    plt.show()


except nx.NodeNotFound:
    print("Error: La ciudad no existe en el grafo.")
except nx.NetworkXNoPath:
    print("No existe una ruta entre las cuidades.")