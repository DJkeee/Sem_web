import pandas as pd
import networkx as nx

def build_graph(filename):
    df = pd.read_excel(filename)
    df.columns = ['Пакет', 'RPM', 'SRPM',"Описание", 'Отношение к ИБ', 'Кандидат на удаление']
    data = df.to_dict('records')

    g = nx.Graph()

    # Добавляем узлы для данных
    g.add_node("RPM")
    g.add_node("SRPM")
    g.add_node("Отношение к ИБ")
    g.add_node("Кандидат на удаление")

    for row in data:
        package_name = row['Пакет']
        g.add_node(package_name)  # Добавляем узел для пакета
        g.add_edge(package_name, "RPM", label=row['RPM'])
        g.add_edge(package_name, "SRPM", label=row['SRPM'])
        g.add_edge(package_name, "Отношение к ИБ", label=row['Отношение к ИБ'])
        g.add_edge(package_name, "Кандидат на удаление", label=row['Кандидат на удаление'])

    return g


def find_packages_by_relation(graph, relation_column, relation_value):
    """Ищет пакеты, имеющие заданное отношение."""
    packages = []
    for node in graph.nodes:
        if graph.has_edge(node, relation_column) and graph[node][relation_column]["label"] == relation_value:
            packages.append(node)
    return packages

def get_relations_for_package(graph, package_name):
    """Получает значения всех отношений для заданного пакета."""
    relations = {}
    for relation_node in ["RPM", "SRPM", "Отношение к ИБ", "Кандидат на удаление"]:
        if graph.has_edge(package_name, relation_node):
            relations[relation_node] = graph[package_name][relation_node]["label"]
    return relations

def found_relations(graph):
    relation_column = input("Введите столбец (RMP, SRMP, Отношение к ИБ,Кандидат на удаление): ")
    relation_value = input(f"Введите значение для '{relation_column}': ")
    found_packages = find_packages_by_relation(graph, relation_column, relation_value)

    # Вывод результата
    if found_packages:
        print(f"Пакеты с '{relation_column}': '{relation_value}':")
        for package in found_packages:
            all_relations = get_relations_for_package(graph, package)
            print(f"  {package}: {all_relations}")
    else:
        print(f"Пакеты с '{relation_column}': '{relation_value}' не найдены.")