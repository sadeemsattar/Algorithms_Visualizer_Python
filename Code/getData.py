import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def getData(fileName, G, G1):
    count = 0
    s = ''
    startNode = 0
    flag = False
    check = False
    count = 0
    nodes = 0
    array = []
    array1 = []
    array2 = []
    row = 0

    with open(fileName, 'r') as data:
        for read in data:
            s = read.split('\t')
            row = row+1
            array2.append(s)
            for x in s:
                if x != '\n':
                    data = re.split('\n', x)
                    # iterator = iter(data)
                    # node = next(iterator)
                    # print(node)
                    for D in data:
                        if D != '' and D != 'NETSIM':
                            if flag == False:
                                nodes = int(D)
                                flag = True
                                # print(D)
                            count = count + 1
                            if count <= nodes*3+1:
                                if check == False:
                                    check = True
                                else:
                                    # print(D)
                                    array.append(float(D))
                            else:
                                array1.append(float(D))

    size = len(array)
    jump = 0
    for j in range(size):
        if jump < nodes*2:
            G.add_node(array[j+jump],
                       pos=(array[j+jump+1], array[j+jump+2]))
            G1.add_node(array[j+jump],
                        pos=(array[j+jump+1], array[j+jump+2]))
            jump = jump+2

    startNode = int(array2[row-1][0])
    size1 = len(array2)

    for i in range(nodes+5, size1-1):
        sizeCheck = len(array2[i])
        edge = array2[i][0]
        for j in range(1, sizeCheck):
            if j % 2 != 0 and array2[i][j] != '\n' and float(array2[i][j]) <= 100:
                G.add_edge(float(edge), float(
                    array2[i][j]), weight=float(array2[i][j+2])/10000000)

    return startNode
