# library snowymontreal
from snowymontreal.solve_aux import *


def solve(is_oriented, num_vertices, edge_list):
    """
    Main function of the library solve
    The path must go through every edges of the graph at least once.
    Find the most optimized path (usually a cycle)
    We suppose the graph is edge connected.

    First, the graph is `eulerized`. Then, a cycle (the path) is found in the
    new graph.
    :param is_oriented:
    :param num_vertices:
    :param edge_list:
    :return: the path found (as a list of vertex)
    """
    edges_list_copy = edge_list[:]
    eulerize(num_vertices, edges_list_copy, is_oriented)
    return find_eulerian_cycle(num_vertices, edges_list_copy, is_oriented)
