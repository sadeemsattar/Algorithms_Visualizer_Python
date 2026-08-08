
import networkx as nx
import matplotlib.pyplot as plt


def PrintGraph(G1):
    pos = nx.get_node_attributes(G1, 'pos')
    labels = nx.get_edge_attributes(G1, 'weight')

    nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels)
    nx.draw(G1, pos, with_labels=True, edge_color='black', node_color="yellow", node_size=600,
            font_size=7, font_family='sans-serif', linewidths=0.25)
    plt.show()
    G1.clear()
