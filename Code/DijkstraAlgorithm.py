
def minDistance(dist, queue):
    minimum = float("Inf")
    min_index = -1
    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index


def DijkstraAlgo(graph, src):

    row = len(graph)
    col = len(graph[0])
    dist = [float("Inf")] * row
    parent = [-1] * row
    dist[src] = 0
    queue = []
    for i in range(row):
        queue.append(i)
    while queue:
        u = minDistance(dist, queue)

        queue.remove(u)

        for i in range(col):

            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u

    return parent
