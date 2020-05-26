# library solve

'''
    First, we take care of the drone.
    The graph used for the drone is a non-oriented graph

    1) first implementation
        Drone: we suppose the graph is non-oriented and is an eulerian graph without weights

    2) second implementation
        Drone: we suppose the graph might not be eulerian. If it is not eulerian, Thus, we must used the weights.
        // FIXME: Find algo
'''


def is_eulerian_non_oriented(num_vertices, edge_list):
    return False

def find_eulerian_cycle_non_oriented(num_vertices, edge_list):
    return False

def solve(is_oriented, num_vertices, edge_list):
    if not is_oriented:
        if is_eulerian_non_oriented(num_vertices, edge_list):
            return find_eulerian_cycle_non_oriented(num_vertices, edge_list)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
