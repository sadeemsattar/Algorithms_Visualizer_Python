
INF = 999999999


def PrimsAlgo(G_matrix, V, start_node, G1):
    print(G_matrix)
    selected = [0]*V
    no_edge = 0
    selected[start_node] = True
    MSTcost = 0.0
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G_matrix[i][j]):
                        if minimum > G_matrix[i][j]:
                            minimum = G_matrix[i][j]
                            x = i
                            y = j
        MSTcost = MSTcost + float(G_matrix[x][y])
        G1.add_edge(x, y, weight=G_matrix[x][y])
        selected[y] = True
        no_edge += 1
    print("Minimum Cost From Prims Algorithm: ", MSTcost)
