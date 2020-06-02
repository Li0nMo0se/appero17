# library solve

"""
    Contain some functions needed by snowymontreal.py
"""


def is_eulerian_cycle(num_vertices, edges_list, cycle):
    """
    Check whether the given cycle is an eulerian cycle in the given graph
    :param num_vertices:
    :param edges_list:
    :param cycle:
    :return:
    """

    def consume(begin, end, edges):
        for i in range(len(edges)):
            if begin == edges[i][0] and end == edges[i][1]:
                edges.pop(i)
                return True
            if begin == edges[i][1] and end == edges[i][0]:
                edges.pop(i)
                return True
        return False

    len_cycle = len(cycle)
    if len(edges_list) != len_cycle:
        return False
    if len(edges_list) == 0:
        return True

    for i in range(len_cycle - 1):
        if not consume(cycle[i], cycle[i + 1], edges_list):
            return False
    if not consume(cycle[len_cycle - 1], cycle[0], edges_list):
        return False
    return edges_list == []


def odd_vertices(num_vertices, edges_list):
    """
    Return a list of the odd vertices
    :param num_vertices:
    :param edges_list:
    :return: list
    """
    deg = [0] * num_vertices
    for (a, b, _) in edges_list:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(num_vertices) if deg[a] % 2]


def even_vertices(num_vertices, edges_list):
    """
    Check whether the vertices of the graph have all a even degree
    :param num_vertices:
    :param edges_list:
    :return: boolean
    """
    deg = [0] * num_vertices
    for (a, b, _) in edges_list:
        deg[a] += 1
        deg[b] += 1
    for a in range(num_vertices):
        if deg[a] % 2 != 0:  # odd deg, incorrect
            return False
    return True


def is_undirected_connected(n, edges):
    if n == 0:
        return True
    # Convert to adjacency list
    succ = adjacency_list(n, edges, False)
    # DFS over the graph
    touched = [False] * n
    touched[0] = True
    todo = [0]
    while todo:
        s = todo.pop()
        for d in succ[s]:
            if not touched[d]:
                touched[d] = True
                todo.append(d)
    somme = sum(touched)
    if somme == n:
        return True
    return False


def is_edge_connected(num_vertices, edges_list):
    """
    Check whether is the graph is edge connected.
    A graph is edge connected if all edges can be visited from one
    :param num_vertices:
    :param edges_list:
    :return: true if the graph is connected, false otherwise
    """
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


def adjacency_list(num_vertices, edges_list, is_oriented=False):
    """
    :param num_vertices:
    :param edges_list:
    :param is_oriented:
    :return: adjacency list of the given graph
    """
    succ = [[] for _ in range(num_vertices)]
    for (a, b, _) in edges_list:
        succ[a].append(b)
        if not is_oriented:
            succ[b].append(a)
    return succ
