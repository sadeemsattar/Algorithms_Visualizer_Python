

Max = 10000000000


def BellmanFord(graph, src, V):
    parent = [-1]*V
    dist = [Max] * V
    dist[src] = 0
    for _ in range(V - 1):

        for u in range(V):
            for v in range(V):
                if graph[u][v] != 0.0:
                    if dist[u] != float("Inf") and dist[u] + graph[u][v] < dist[v]:
                        dist[v] = dist[u] + graph[u][v]
                        parent[v] = u

    for u in range(V):
        for v in range(V):
            if graph[u][v] != 0.0:
                if dist[u] != float("Inf") and dist[u] + graph[u][v] < dist[v]:
                    print("Graph contains negative weight cycle")
                    return

    return parent
