class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = []

    def add_node(self, node):
        if not node in self.graph:
            self.graph[node] = []
            self.nodes.append(node)

    def add_edge(self, edge):
        node1 = edge.get_node1()
        node2 = edge.get_node2()
        self.add_node(node1)
        self.add_node(node2)
        present = False
        for sublist in self.graph[node1]:
            if node2 in sublist:
                present = True
                break
        if not present:
            self.graph[node1].append([node2, edge.get_time()])
        for sublist in self.graph[node2]:
            if node1 in sublist:
                present = True
                break
        if not present:
            self.graph[node2].append([node1, edge.get_time()])

    def remove_edge(self, node1, node2):
        for i in self.graph[node1]:
            if i[0] == node2:
                self.graph[node1].remove(i)
        for i in self.graph[node2]:
            if i[0] == node1:
                self.graph[node2].remove(i)
        if len(self.graph[node1]) == 0:
            if node1 in self.nodes:
                self.nodes.remove(node1)
            if node1 in self.graph:
                del self.graph[node1]
        if len(self.graph[node2]) == 0:
            if node2 in self.nodes:
                self.nodes.remove(node2)
            if node2 in self.graph:
                del self.graph[node2]

    def get_neighbors(self, node):
        return self.graph[node]

    def __str__(self):
        string = ""
        for node1 in self.graph:
            for to in self.graph[node1]:
                string += f"{node1} ---> {to[0]}  {to[1]}\n"
        string = string[:-1]
        return string

    def dijkstra(self, inicio, final):
        actual = inicio
        noVisitados = graph.nodes
        padres = {}
        visitados = {}
        distancias = {actual: 0}
        for i in self.nodes:
            if i != actual:
                distancias[i] = float("inf")
            padres[i] = None
            visitados[i] = False

        while len(noVisitados) > 0:
            for vecino in self.graph[actual]:
                if not visitados[vecino[0]]:
                    if distancias[actual] + vecino[1] < distancias[vecino[0]]:
                        distancias[vecino[0]] = distancias[actual] + vecino[1]
                        padres[vecino[0]] = actual
            visitados[actual] = True
            noVisitados.remove(actual)

            if len(noVisitados) > 0:
                m = distancias[noVisitados[0]]
                actual = noVisitados[0]
                for e in noVisitados:
                    if m > distancias[e]:
                        m = distancias[e]
                        actual = e

        camino = []
        actual = final
        while actual != None:
            camino.insert(0, actual)
            actual = padres[actual]

        return [camino, distancias[final]]


class Edge:
    def __init__(self, node1, node2, time):
        self.node1 = node1
        self.node2 = node2
        self.time = time

    def get_node1(self):
        return self.node1

    def get_node2(self):
        return self.node2

    def get_time(self):
        return self.time

    def __str__(self):
        return f"{self.node1}->{self.node2} {self.time}"


graph = Graph()

# Primera Linea
entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])

# Segunda Linea
entrada = input().split()
P = int(entrada[0])
C = int(entrada[1])

# Tercera Linea
T = input()

# M Lineas
for i in range(int(M)):
    entrada = input().split()
    U = int(entrada[0])
    V = int(entrada[1])
    D = int(entrada[2])
    graph.add_edge(Edge(str(U), str(V), D))

resultado = graph.dijkstra(str(C), str(P))
camino_mas_corto = resultado[0]
tiempo_minimo = resultado[1]
if tiempo_minimo > int(T):
    print(
        "Bowser se lleva a la princesa (Cuando Mario no logra llegar a la base donde se encuentra la princesa antes que acabe el tiempo)"
    )

for i in range(len(camino_mas_corto) - 1):
    graph.remove_edge(camino_mas_corto[i], camino_mas_corto[i + 1])

# tiempo_minimo += graph.dijkstra(str(P), str(C))[1]
# if tiempo_minimo > int(T):
#     print(
#         "Bowser te atrapa con la princesa (Cuando Mario no logra volver al castillo con la princesa antes que acabe el tiempo o ya no existe un camino para volver"
#     )
# else:
#     print(
#         "La princesa es salvada (Cuando Mario logra rescatar y volver con la princesa al castillo antes que acabe el tiempo)"
#     )
