import osmnx as ox

def to_reg_graph(osmnx_graph, is_oriented=True):
    nodes = list(osmnx_graph.nodes)
    osmnx_edges = list(osmnx_graph.edges)
    edges = []
    for elt in osmnx_edges:
        edges.append((nodes.index(elt[0]), nodes.index(elt[1]), elt[2]))
    if not is_oriented:
        for elt in edges:
            if (edges.count(elt) > 1 or (edges.count((elt[1], elt[0], elt[2])))):
                edges.remove(elt)
    return (len(nodes), edges)
