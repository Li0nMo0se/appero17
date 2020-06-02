from graphviz import Digraph
from graphviz import Graph

# open a pdf with the graph printed
def print_graph(num_vertices, edges_list, is_oriented = False):
    
    if (is_oriented):
        dot = Digraph('graph')
    else:
        dot = Graph('graph')

    for i in range(0, num_vertices):
        dot.node(str(i), str(i))

    for (a,b) in edges_list:
        dot.edge(str(a),str(b))

    dot.view()
