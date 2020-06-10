import osmnx as ox

def to_reg_graph(osmnx_graph):
    nodes = list(osmnx_graph.nodes)
    osmnx_edges = list(osmnx_graph.edges)
    edges = []
    for elt in osmnx_edges:
        edges.append((nodes.index(elt[0]), nodes.index(elt[1]), elt[2]))
    return (len(nodes), edges)
