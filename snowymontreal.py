# library snowymontreal
from solve_aux import *


"""
    Solve:
    The implementation of the function solve has been made by iterations. 
    1) First implementation:
        First, we take care of the drone. Hence, we suppose the graph is 
        non-oriented and is an eulerian graph without weights. Then, we simply 
        need to find an eulerian cycle in an eulerian graph.

    2) Second implementation:
        Drone: we suppose the graph might not be eulerian. If it is not 
        eulerian, we might use an edge several times but at least once. In this 
        case, we have to create additional edges in order to make the graph 
        eulerian. The edges are added without any specific order. We call this 
        operation `eulerize` the graph

    3) Third implementation:
        Now, we want to use the weights to minimize the cost. Also, weights 
        corresponds to a distance between two intersection. And a distance is 
        always positive. So, the weights are also always positive. We won't
        encounter negative cycles.
        We try to be smarter in the way we create the additional edges by
        minimizing the cost of the created edges.
    
    4) Fourth implementation:
        We have been taking care of the drone with an undirected graph. In 
        this new iteration, we want to find a path for the `déneigeuse`. This
        time, the vehicles must follow the direction of the streets. Thus, 
        we use an oriented graph. Similarly, we `eulerize` an oriented graph.
        The algorithm to do so in quite different as for the non-oriented graph.
    
    Tests:
    
    Many unit tests are made (in the file eulerian_tests.py). It tests every 
    auxiliary function needed by `solve`. By this way, it is easy to improve 
    the program by iterations.
"""


def solve(is_oriented, num_vertices, edges_list):
    """
    Main function of the library solve
    The path must go through every edges of the graph at least once.
    Find the most optimized path (usually a cycle)
    We suppose the graph is edge connected.

    First, the graph is `eulerized`. Then, a cycle (the path) is found in the
    new graph.
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :return: the path found (as a list of vertex)
    """
    eulerize(num_vertices, edges_list, is_oriented)
    return find_eulerian_cycle(num_vertices, edges_list, is_oriented=False)
