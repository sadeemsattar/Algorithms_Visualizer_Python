

INF = 99999999999999999


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def boruvkaMST(G, V, G1):
    parent = []
    rank = []
    cheapest = []
    numTrees = V
    MSTweight = 0

    for node in range(V):
        parent.append(node)
        rank.append(0)
        cheapest = [-1] * V

    k = 0
    while numTrees > 1:

        for i in range(len(G)):
            for k in range(len(G)):

                if G[k][i] != 0:
                    u = k
                    v = i
                    w = G[k][i]
                    print(k, i, w)

                    set1 = find(parent, u)
                    set2 = find(parent, v)

                    if set1 != set2:

                        if cheapest[set1] == -1 or cheapest[set1][2] > w:
                            cheapest[set1] = [u, v, w]

                        if cheapest[set2] == -1 or cheapest[set2][2] > w:
                            cheapest[set2] = [u, v, w]

        for node in range(V):

            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                set1 = find(parent, u)
                set2 = find(parent, v)

                if set1 != set2:
                    MSTweight += w
                    union(parent, rank, set1, set2)

                    G1.add_edge(u, v, weight=w)

                    numTrees = numTrees - 1

        cheapest = [-1] * V

    print("Weight of MST is %d" % MSTweight)
