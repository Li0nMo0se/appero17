import osmnx as ox
from print import *

def to_reg_graph(osmnx_graph, is_oriented=True):
    if not is_oriented:
        osmnx_graph = ox.utils_graph.get_undirected(osmnx_graph)
    nodes = list(osmnx_graph.nodes)
    osmnx_edges = list(osmnx_graph.edges)
    edges = []
    for elt in osmnx_edges:
        edges.append((nodes.index(elt[0]), nodes.index(elt[1]), elt[2]))
    return (len(nodes), edges)

G = ox.graph_from_place('Caubous, FR', network_type='drive')
(nodes, edges) = to_reg_graph(G, False)
print_graph(nodes, edges)
# info = ox.utils_graph.get_route_edge_attributes(G, (2284607031, 2284607123))
# info = ox.utils_graph.get_route_edge_attributes(G, (2283549807, 2283247033), 'length')
# print(ox.utils_graph.get_undirected(G).edges)
# print(info)
# ox.plot_graph(G)
