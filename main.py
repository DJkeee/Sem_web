from graph_funcs import *
from graph_visualizer import *

if __name__ == "__main__":
    graph = build_graph('database.xlsx')
    visualize_graph(graph)
    found_relations(graph)

