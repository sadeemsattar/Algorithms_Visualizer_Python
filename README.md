# Graph Algorithms Visualizer

A desktop tool for running classic graph algorithms on benchmark network files and visualizing the results. Built with Tkinter for the GUI and NetworkX + Matplotlib for graph construction and plotting.

University project (algorithms course). The accompanying project report is in [`docs/ALGO PROJECT REPORT.docx`](docs/).

## What it does

You pick a benchmark graph (10–100 nodes) and an algorithm from a small Tkinter window. The program parses the corresponding NETSIM-format input file into a NetworkX graph, runs the algorithm, prints the resulting cost to the terminal, and opens a Matplotlib window showing the computed subgraph (MST or shortest-path tree) with edge weights.

### Algorithms implemented

| Algorithm | Type | Implementation |
|---|---|---|
| Prim's | Minimum spanning tree | `src/PrimsAlgorithm.py` |
| Kruskal's | Minimum spanning tree | `src/KruskalAlgorithm.py` |
| Boruvka's | Minimum spanning tree | `src/boruvkasMST.py` |
| Dijkstra's | Single-source shortest paths | `src/DijkstraAlgorithm.py` |
| Bellman-Ford | Single-source shortest paths | `src/BellmenFordAlgorithm.py` |
| Floyd-Warshall | All-pairs shortest paths | `src/FloydWarshallAlgorithm.py` |
| Clustering coefficient | Graph metric (via NetworkX) | `src/ClusteringCoefficient.py` |

The MST and shortest-path algorithms are implemented from scratch on adjacency matrices; only the clustering coefficient delegates to NetworkX built-ins.

## Project structure

```
src/                  Application code
  Interface.py        Entry point: Tkinter GUI, wires inputs to algorithms
  getData.py          Parses NETSIM benchmark files into NetworkX graphs
  PrintGraph.py       Draws a graph with edge-weight labels via Matplotlib
  <Algorithm>.py      One module per algorithm (see table above)
data/                 Benchmark inputs: input10.txt ... input100.txt
                      (NETSIM format, 10-100 nodes in steps of 10)
docs/                 Original project report (.docx)
```

## Prerequisites

- Python 3.9+ with Tkinter (included in the python.org installer; on Debian/Ubuntu install `python3-tk`)
- pip packages: see `requirements.txt` (networkx, matplotlib, pandas, numpy)

## Setup and run

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python src/Interface.py
```

In the window that opens:

1. Choose a node count (10–100) from the lower dropdown and click **Select Number Of Nodes** — this loads `data/input<N>.txt` (the loaded filename is echoed in the terminal).
2. Choose an algorithm from the upper dropdown and click **Select Algo To Apply** — the result graph opens in a Matplotlib window and the cost is printed to the terminal.
3. Close the graph window to run another algorithm; close the main window to exit.

Input files are resolved relative to the repository, so the program can be launched from any working directory.

## Input format

The `data/input<N>.txt` files are NETSIM exports: a node count, then one line per node with its 2D coordinates (used for plot layout), then adjacency records with per-edge bandwidth/weight values (weights are scaled by 1e7 during parsing).

## Known limitations

- Load a graph (step 1) before applying an algorithm — running an algorithm first operates on an empty graph and errors.
- Dijkstra and Bellman-Ford always start from a fixed source node: the start node parsed from the input file is not propagated to the GUI handler (a shadowed-variable bug in `Interface.py`, left as-is to preserve original behavior).
- Results and costs are printed to the terminal rather than shown in the GUI.
- No tests; error handling is minimal (invalid/missing input files raise uncaught exceptions).
- Verified headless (module imports, input parsing, and Prim's on `input10.txt`); the full GUI flow follows the original project's design but was not re-verified end-to-end in this cleanup.

## Status

Complete as a coursework project; not under active development.
