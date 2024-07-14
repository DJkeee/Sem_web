import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(graph, seed=42)  # Алгоритм расстановки узлов

    # Рисуем узлы
    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=700,
        node_color="lightblue",
        edgecolors="black",
        linewidths=1.5
    )


    nx.draw_networkx_edges(
        graph,
        pos,
        width=2,
        alpha=0.7,
        edge_color="gray"
    )

    # Добавляем метки узлов
    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=12,
        font_color="black",
        font_weight="bold"
    )

    # Добавляем метки ребер
    edge_labels = nx.get_edge_attributes(graph, 'label')
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels,
        font_size=10,
        font_color="black",
        label_pos=0.5,
        rotate=False,
        font_family="Arial"
    )

    plt.axis("off")
    plt.tight_layout()

    plt.show()