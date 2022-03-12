from tkinter import *

from networkx.generators.geometric import euclidean
from ClusteringCoefficient import ClusteringCoefficient
from FloydWarshallAlgorithm import FloydWarshallAlgo
from getData import *
from PrintGraph import *
from BellmenFordAlgorithm import *
from PrimsAlgorithm import *
from DijkstraAlgorithm import *
from KruskalAlgorithm import*
from boruvkasMST import *
import pandas as pd
import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
INF = 9999999
# create canvas
root = Tk()
Heading = Label(root, text="Algorithms")

# store number of nodes
no_of_nodes = ''
# store algorithm to apply
algo_to_apply = ""
startNode = 0

G = nx.Graph()
G1 = nx.Graph()

# function to store algo name


def selected():
    G1.clear()
    G.clear()
    no_of_nodes = click.get()
    if no_of_nodes != 0:
        fileName = "input"+no_of_nodes+".txt"
        print(fileName)
        startNode = getData(fileName, G, G1)
        # print(startNode)
    return


def select():
    algo_to_apply = clicked.get()
    V = click.get()
    cost = 0.0
    if algo_to_apply == "PrimsAlgo":
        matrix = nx.to_pandas_adjacency(G)
        # print(matrix)
        PrimsAlgo(matrix, int(V), 2, G1)
        PrintGraph(G1)

    elif algo_to_apply == "KruskalAlgo":
        matrix = nx.to_pandas_adjacency(G)
        for i in range(int(V)):
            for j in range(int(V)):
                if matrix[i][j] == 0.0:
                    matrix[i][j] = INF
        print(int(V))
        kruskalMST(matrix, int(V), G1)
        PrintGraph(G1)

    elif algo_to_apply == "DijkstraAlgo":
        matrix = nx.to_pandas_adjacency(G)
        # print(matrix)
        arrayColumn = DijkstraAlgo(matrix,  startNode+1)
        pathSize = len(arrayColumn)
        for j in range(pathSize):
            if arrayColumn[j] != -1:
                # print(arrayColumn[j], arrayColumn[j+1])
                cost = cost + float(matrix[arrayColumn[j]][j])
                G1.add_edge(arrayColumn[j], j,
                            weight=matrix[arrayColumn[j]][j])

        print("Minimum cost From Dijkstra Algorithm: ", cost)
        PrintGraph(G1)

    elif algo_to_apply == "FloydWarshallAlgo":
        matrix = nx.to_pandas_adjacency(G)

        for i in range(int(V)):
            for j in range(int(V)):
                if matrix[i][j] == 0.0 and i != j:
                    matrix[i][j] = INF
                elif i == j:
                    matrix[i][j] = 0.0
        # print(matrix)
        FloydWarshallAlgo(matrix, int(V), G1)
        PrintGraph(G1)

    elif algo_to_apply == "BoruvkasAlgo":
        matrix = nx.to_pandas_adjacency(G)
        boruvkaMST(matrix, int(V), G1)
        PrintGraph(G1)
    elif algo_to_apply == "BellmenFordAlgo":
        matrix = nx.to_pandas_adjacency(G)

        p = BellmanFord(matrix, startNode+1, int(V))
        for i in range(int(V)):
            if p[i] != -1:
                G1.add_edge(p[i], i, weight=matrix[p[i]][i])
                cost = cost+float(matrix[p[i]][i])
        print("Minimun Cost From BellmenFordAlgorithm : ", cost)
        PrintGraph(G1)

    elif algo_to_apply == "ClusteringCoefficeint":
        ClusteringCoefficient(G)
    cost = 0.0

    return

 # menue for algorithm selection
options = [
    "PrimsAlgo",
    "KruskalAlgo",
    "DijkstraAlgo",
    "BellmenFordAlgo",
    "FloydWarshallAlgo",
    "ClusteringCoefficeint",
    "BoruvkasAlgo"]

# menue for nodes selction
nodes = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
Heading.pack()

SelectNodes = Label()
SelectNodes.pack()
clicked = StringVar()
clicked.set(options[0])

# show algo menue
drop1 = OptionMenu(root, clicked, *options)
drop1.pack()
myButton1 = Button(root, text="Select Algo To Apply", command=select)
myButton1.pack()

# show nodes selction menue
click = StringVar()
click.set(nodes[0])
drop2 = OptionMenu(root, click, *nodes)
drop2.pack()
myButton = Button(root, text="Select Number Of Nodes", command=selected)
myButton.pack()

root.mainloop()
