from graphviz import Digraph
from graphviz import Graph
import networkx as nx
import random
import osmnx as ox


def generate_connected_undirected_graph(num_vertices, directed=False):
    """
    Generate a random graph with num_vertices and num_edges
    :param num_vertices:
    :return: a graph
    """

    G = nx.erdos_renyi_graph(num_vertices, 0.5, seed=123, directed=directed)
    edges_list = []
    for (u, v) in G.edges():
        edges_list.append((u, v, random.randint(0, 1000)))
    return len(G.nodes), edges_list


def make_graph(num_vertices, edges_list, is_oriented=False, name="graph"):
    """
    Convert a graph to the dot format
    :param num_vertices:
    :param edges_list:
    :param is_oriented:
    :param name:
    :return: the graph represented by the dot format
    """
    if is_oriented:
        dot = Digraph(name)
    else:
        dot = Graph(name)

    for i in range(0, num_vertices):
        dot.node(str(i), str(i))

    for (a, b, label) in edges_list:
        dot.edge(str(a), str(b), str(label))
    return dot


def print_graph(num_vertices, edges_list, is_oriented=False, name="graph"):
    """
    open a pdf with the graph printed
    :param num_vertices:
    :param edges_list:
    :param is_oriented:
    :param name:
    """
    dot = make_graph(num_vertices, edges_list, is_oriented, name)
    dot.view()


def save_graph(num_vertices, filename, edges_list, is_oriented=False,
                name="graph"):
    """
    Save a graph in a file
    :param num_vertices:
    :param filename:
    :param edges_list:
    :param is_oriented:
    :param name:
    """
    dot = make_graph(num_vertices, edges_list, is_oriented, name)
    dot.save(filename + ".gv")


def to_reg_graph(osmnx_graph, is_oriented=False):
    """
    Convert an osmnx graph to a regular graph (the ones used in the
    snowymontreal library
    :param osmnx_graph:
    :param is_oriented:
    :return:
    """
    if not is_oriented:
        osmnx_graph = ox.utils_graph.get_undirected(osmnx_graph)
    nodes = list(osmnx_graph.nodes)
    osmnx_edges = list(osmnx_graph.edges)
    edges = []
    for elt in osmnx_edges:
        l = ox.utils_graph.get_route_edge_attributes(osmnx_graph,
            (elt[0], elt[1]), 'length')
        edges.append((nodes.index(elt[0]), nodes.index(elt[1]), l[0]))
    return len(nodes), edges

