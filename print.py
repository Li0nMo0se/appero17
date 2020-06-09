from graphviz import Digraph
from graphviz import Graph


def print_graph(num_vertices, edges_list, is_oriented=False, name="graph"):
    """
        open a pdf with the graph printed
    """
    if is_oriented:
        dot = Digraph(name)
    else:
        dot = Graph(name)

    for i in range(0, num_vertices):
        dot.node(str(i), str(i))

    for (a, b, label) in edges_list:
        dot.edge(str(a), str(b), str(label))

    dot.view()
