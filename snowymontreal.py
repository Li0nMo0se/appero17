# library solve
from solve_help import *


def is_eulerian_non_oriented(num_vertices, edges_list):
    """
    A graph is eulerian if it has a eulerian cycle.
    Or if all degrees are even and the edges are all connected
    :param num_vertices:
    :param edges_list:
    :return: boolean whether the graph is eulerian
    """
    return even_vertices(num_vertices, edges_list) and is_edge_connected(num_vertices, edges_list)


def find_eulerian_cycle_non_oriented(num_vertices, edges_list):
    def consume(curr, edges, seen, cycle, first=-1):
        cycle.append(curr)
        if first == -1:
            first = curr
        elif curr == first:  # cycle done
            return False
        for i in range(len(edges)):
            if seen[i]:
                continue
            if edges[i][0] == curr:
                seen[i] = True
                consume(edges[i][1], edges, seen, cycle, first)
                return True
            elif edges[i][1] == curr:
                seen[i] = True
                consume(edges[i][0], edges, seen, cycle, first)
                return True
        return False

    # it must be an eulerian graph
    assert is_eulerian_non_oriented(num_vertices, edges_list)

    # Specific cases
    if not edges_list:
        return []
    if len(edges_list) == 1:
        return [edges_list[0][0]]

    # General case
    seen = [False] * len(edges_list)
    cycle = []
    consume(edges_list[0][0], edges_list, seen, cycle)
    cycle.pop()
    must_continue = True
    while must_continue:
        for i in range(len(cycle)):
            new_cycle = []
            if not consume(cycle[i], edges_list, seen, new_cycle):
                continue
            new_cycle.pop()
            cycle[i:i] = new_cycle
            break
        must_continue = False
        for seen_ in seen:
            if not seen_:
                must_continue = True
    return cycle


def eulerize(num_vertices, edges_list, is_oriented=False):
    """
    Update a undirected graph to eulerian graph. Will modify the graph itself by adding edges.
    If the graph is already an eulerian graph. Nothing is updated.
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :return: None
    """
    odd = odd_vertices(num_vertices, edges_list, is_oriented)
    for i in range(0, len(odd) - 1, 2):
        first_vertex = odd[i]
        second_vertex = odd[i + 1]
        path = find_shortest_path(num_vertices, edges_list, first_vertex, second_vertex)
        # Create the new edges according to the path
        for v in range(0, len(path) - 1):
            src, cost = path[v]
            dst, _ = path[v + 1]
            edges_list.append((src, dst, cost))  # does not take care of the costs


"""
    First, we take care of the drone.
    The graph used for the drone is a non-oriented graph

    1) first implementation
        Drone: we suppose the graph is non-oriented and is an eulerian graph without weights

    2) second implementation
        Drone: we suppose the graph might not be eulerian. If it is not eulerian, we might use an edge several times.
        We want to find a path that uses every edges at least once. In this case, we have to create additional edges in
        order to make the graph eulerian.

    3) third implementation:
        Now, we want to use the weights to minimize the cost. Also, weights corresponds to a distance and a distance is
        always positive. So, the weights are also always positive. We won't encounter negative cycles.
        We try to be smarter in the way we create the additional edges by minimizing the cost of the created edges.
"""


def solve(is_oriented, num_vertices, edges_list):
    """
    Main function of the library solve
    Find the most optimized path (usually a cycle)
    There are several ways to find the best path depending of the type of the graph
    We suppose the graph is edge connected
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :return: the path found (as a list of vertex)
    """
    if not is_oriented:
        eulerize(num_vertices, edges_list, is_oriented)
        return find_eulerian_cycle_non_oriented(num_vertices, edges_list)
    else:
        raise NotImplementedError
