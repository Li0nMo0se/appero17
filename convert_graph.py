import osmnx as ox

def to_reg_graph(osmnx_graph, is_oriented=False):
    if not is_oriented:
        osmnx_graph = ox.utils_graph.get_undirected(osmnx_graph)
    nodes = list(osmnx_graph.nodes)
    osmnx_edges = list(osmnx_graph.edges)
    edges = []
    for elt in osmnx_edges:
        l = ox.utils_graph.get_route_edge_attributes(osmnx_graph, (elt[0], elt[1]), 'length')
        edges.append((nodes.index(elt[0]), nodes.index(elt[1]), l[0]))
    return (len(nodes), edges)
