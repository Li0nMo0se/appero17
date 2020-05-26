# library solve
from solve_help import *

'''
    First, we take care of the drone.
    The graph used for the drone is a non-oriented graph

    1) first implementation
        Drone: we suppose the graph is non-oriented and is an eulerian graph without weights

    2) second implementation
        Drone: we suppose the graph might not be eulerian. If it is not eulerian, Thus, we must used the weights.
        // FIXME: Find algo
'''

def is_eulerian_non_oriented(num_vertices, edges_list):
    '''
        A graph is eulerian if it has a eulerian cycle.
        Or if all degrees are even and the edges are all connected
    :param num_vertices:
    :param edges_list:
    :return: boolean whether the graph is eulerian
    '''

    def even_vertices(num_vertices, edges_list):
        deg = [0] * num_vertices
        for (a, b, _) in edges_list:
            deg[a] += 1
            deg[b] += 1
        for a in range(num_vertices):
            if deg[a] % 2 != 0:  # odd deg, incorrect
                return False
        return True

    def is_edge_connected(num_vertices, edges_list):
        if num_vertices == 0 or len(edges_list) == 0:
            return True
        succ = adjacency_list(num_vertices, edges_list)
        seen = [False] * num_vertices
        init = edges_list[0][0]  # random vertex
        seen[init] = True
        todo = [init]
        while todo:
            s = todo.pop()
            for d in succ[s]:
                if not seen[d]:
                    seen[d] = True
                    todo.append(d)
        return all(seen[a] or not succ[a] for a in range(num_vertices))
        
    return even_vertices(num_vertices, edges_list) and is_edge_connected(num_vertices, edges_list)


def find_eulerian_cycle_non_oriented(num_vertices, edges):
    '''edges = edges_list
    print(edges)
    print('\n')
    print('Y')
    print('\n')
    print(edges_list)
    print ('\n')'''
    assert is_eulerian_non_oriented(num_vertices, edges)
    if len(edges) == 0:
        return []
    cycle = [edges[0][0]] # start somewhere
    while True:
        rest = []
        for (a, b) in edges:
            if cycle[-1] == a:
                cycle.append(b)
            elif cycle[-1] == b:
                cycle.append(a)
            else:
                rest.append((a,b))
        if not rest:
            assert cycle[0] == cycle[-1]
            return cycle[0:-1]
        edges = rest
        if cycle[0] == cycle[-1]:
            # Rotate the cycle so that the last state
            # has some outgoing edge in EDGES.
            for (a, b) in edges:
                if a in cycle:
                    idx = cycle.index(a)
                    cycle = cycle[idx:-1] + cycle[0:idx+1]
                    break



def solve(is_oriented, num_vertices, edges_list):
    if not is_oriented:
        if is_eulerian_non_oriented(num_vertices, edges_list):
            return find_eulerian_cycle_non_oriented(num_vertices, edges_list)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
