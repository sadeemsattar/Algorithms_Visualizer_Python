INF = 9999999


def FloydWarshallAlgo(matrix, V, G1):
    graph = matrix
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                if i != j:
                    G1.add_edge(i, j, weight="{:.2f}".format(graph[i][j]))

    return
