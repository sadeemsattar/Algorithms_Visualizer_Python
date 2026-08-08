import networkx as nx


def ClusteringCoefficient(G1):
    print("For Average :", nx.clustering(G1))
    print("")
    print("For Average :", nx.average_clustering(G1))
