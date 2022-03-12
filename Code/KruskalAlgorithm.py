

INF = float('inf')


def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(parent, i, j):
    a = find(parent, i)
    b = find(parent, j)
    parent[a] = b


def kruskalMST(G_matrix, V, G1):
    parent = [i for i in range(V)]
    mincost = 0  # Cost of min MST
    for i in range(V):
        parent[i] = i

    edge_count = 0.0
    while edge_count < V - 1:
        min = INF
        a = -1.0
        b = -1.0
        for i in range(V):
            for j in range(V):
                if find(parent, i) != find(parent, j) and G_matrix[i][j] < min:
                    min = G_matrix[i][j]
                    a = i
                    b = j
        union(parent, a, b)

        G1.add_edge(a, b, weight=min)
        edge_count += 1
        mincost += min

    print("Minimum Cost From Kruskal Algorithm= {}".format(mincost))
