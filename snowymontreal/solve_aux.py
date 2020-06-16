import math

"""
# TODO
"""


def is_eulerian(num_vertices, edges_list, is_oriented=False):
    """
    A graph is eulerian if it has a eulerian cycle.
    Or if all degrees are even and the edges are all connected
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :return: boolean whether the graph is eulerian
    """
    return test_vertices_eulerian(num_vertices, edges_list, is_oriented) \
           and is_edge_connected(num_vertices, edges_list, is_oriented)


def is_eulerian_cycle(num_vertices, edges_list, is_oriented, cycle):
    """
    Check whether the given cycle is an eulerian cycle in the given graph
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :param cycle:
    :return: boolean
    """

    def consume(begin, end, edges):
        for i in range(len(edges)):
            if begin == edges[i][0] and end == edges[i][1]:
                edges.pop(i)
                return True
            if not is_oriented and begin == edges[i][1] and end == edges[i][0]:
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


def odd_vertices_undirected(num_vertices, edges_list):
    """
    Check whether the vertices are odd
    :param num_vertices:
    :param edges_list:
    :return: list of odd vertices
    """
    deg = [0] * num_vertices
    for (a, b, _) in edges_list:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(num_vertices) if deg[a] % 2]


def in_out_deg_directed(num_vertices, edges_list):
    """
    Computer the in degrees and out degrees of a directed graph
    :param num_vertices:
    :param edges_list:
    :return:
    """
    in_deg = [0] * num_vertices
    out_deg = [0] * num_vertices
    for (a, b, _) in edges_list:
        out_deg[a] += 1
        in_deg[b] += 1
    return in_deg, out_deg


def test_vertices_eulerian(num_vertices, edges_list, is_oriented=False):
    """
    Check whether the vertices comply with an eulerian graph requirements
    if not is_oriented: Only even vertices
    if is_oriented: in_deg equals with out_deg for each vertex. In other words,
    every vertices are balanced
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :return: list
    """

    if is_oriented:
        in_deg, out_deg = in_out_deg_directed(num_vertices, edges_list)
        unbalanced = [a for a in range(num_vertices) if in_deg[a] != out_deg[a]]
        return len(unbalanced) == 0
    else:
        return len(odd_vertices_undirected(num_vertices, edges_list)) == 0


def is_connected(n, edges, is_oriented=False):
    if n == 0:
        return True
    # Convert to adjacency list
    succ = adjacency_list(n, edges, is_oriented)
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


def is_edge_connected(num_vertices, edges_list, is_oriented=False):
    """
    Check whether is the graph is edge connected.
    A graph is edge connected if all edges can be visited from one
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    :return: true if the graph is connected, false otherwise
    """
    if num_vertices == 0 or len(edges_list) == 0:
        return True
    succ = adjacency_list(num_vertices, edges_list, is_oriented)
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


def find_shortest_path(num_vertices, edges_list, src, dst, is_oriented=False):
    # Classic Bellman-Ford for undirected graphs
    dist = [math.inf] * num_vertices
    dist[src] = 0
    parent = list(range(num_vertices))
    for k in range(num_vertices - 1):
        for (s, d, w) in edges_list:
            if dist[d] > dist[s] + w:
                parent[d] = (s, w)
                dist[d] = dist[s] + w
            if not is_oriented and dist[s] > dist[d] + w:
                parent[s] = (d, w)
                dist[s] = dist[d] + w

    # src not connected to dst
    if dist[dst] == math.inf:
        return None

    # Extra loop to detect negative cycles
    for (s, d, w) in edges_list:
        if dist[d] > dist[s] + w or (
                not is_oriented and dist[s] > dist[d] + w):
            return None

    # Build the shortest-path from parents
    # In addition, store the cost
    sp = [(dst, 0)]
    while dst != src:
        dst, cost = parent[dst]
        sp.insert(0, (dst, cost))
    return sp


def floyd_warshall(num_vertices, edges_list):
    """
    Floyd warshall algorithm for a directed graph
    Find shortest path from n sources to n destinations
    There isn't any negastive cycle. Only positive weight
    :param num_vertices:
    :param edges_list:
    :return:
    """

    def init_mat(num_vertices, edges_list):
        #  Set up the matrix
        M = [[math.inf for _ in range(num_vertices)]
             for _ in range(num_vertices)]
        #  Matrix for the successors of each vertex
        succ = [[None for _ in range(num_vertices)]
                for _ in range(num_vertices)]

        # Diag elems
        for i in range(num_vertices):
            M[i][i] = 0
            succ[i][i] = i

        # Add the edges
        for (a, b, w) in edges_list:
            M[a][b] = w
            succ[a][b] = b

        return M, succ

    M, succ = init_mat(num_vertices, edges_list)
    for k in range(num_vertices):
        for s in range(num_vertices):
            for u in range(num_vertices):
                old = M[s][u]
                M[s][u] = min(M[s][u], M[s][k] + M[k][u])
                if old != M[s][u]:
                    succ[s][u] = succ[s][k]
    return M, succ


def find_unbalanced_directed(num_vertices, edges_list):
    """
    Find the unbalanced vertices
    A unbalanced vertex is a vertex such that its in_deg != out_deg
    :param num_vertices:
    :param edges_list:
    :return:
    """
    in_deg, out_deg = in_out_deg_directed(num_vertices, edges_list)

    # Set of vertices with a positive degree or negative degree
    delta = []
    set_pos = []
    set_neg = []
    for i in range(num_vertices):
        curr_delta = out_deg[i] - in_deg[i]
        delta.append(curr_delta)
        if curr_delta > 0:
            set_pos.append(i)
        elif curr_delta < 0:
            set_neg.append(i)
    return delta, set_pos, set_neg


def find_feasible(num_vertices, edges_list):
    f = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    delta, set_pos, set_neg = find_unbalanced_directed(num_vertices, edges_list)
    for u in range(len(set_neg)):
        i = set_neg[u]
        for v in range(len(set_pos)):
            j = set_pos[v]
            if -delta[i] < delta[j]:
                f[i][j] = -delta[i]
            else:
                f[i][j] = delta[j]
            delta[i] += f[i][j]
            delta[j] -= f[i][j]
    return f, set_pos, set_neg


def update_graph(edges_list, f, set_pos, set_neg, M, succ):

    def add_edges(edges_list, src, dst, M, succ):
        if succ[src][dst] is None:
            return

        while src != dst:
            tmp = succ[src][dst]
            edges_list.append((src, tmp, M[src][tmp]))
            src = tmp

    for u in range(len(set_neg)):
        i = set_neg[u]
        for v in range(len(set_pos)):
            j = set_pos[v]
            for _ in range(f[i][j]):
                add_edges(edges_list, i, j, M, succ)


def find_eulerian_cycle(num_vertices, edges_list, is_oriented=False):
    if len(edges_list) == 0:  # empty graph
        return []

    cycle = [edges_list[0][0]]  # start somewhere
    while True:
        remaining = []
        for (a, b, w) in edges_list:
            if cycle[-1] == a:
                cycle.append(b)
            elif not is_oriented and cycle[-1] == b:
                cycle.append(a)
            else:
                remaining.append((a, b, w))
        if not remaining:
            return cycle[0:-1]

        edges_list = remaining
        if cycle[0] == cycle[-1]:
            # Rotate the cycle so that the last state
            # has some outgoing edge in EDGES.
            for (a, b, w) in edges_list:
                if a in cycle:
                    idx = cycle.index(a)
                    cycle = cycle[idx:-1] + cycle[0:idx+1]
                    break

def sort_odd(num_vertices, edges_list, odd, is_oriented):
    my_list = []
    do_continue = False
    for i in range(len(odd)):
        for j in range(i + 1, len(odd)):
            path = find_shortest_path(num_vertices, edges_list, odd[i], odd[j])
            print(path)
            if len(path) > 2:
                for k in odd:
                    for z in range(1, len(path)):
                        if (path[1][0] == k):
                            do_continue = True
                if (do_continue == True):
                    do_continue = False
                    continue
            for v in range(0, len(path) - 1):
                src, cost = path[v]  # cost from src to dst
                dst, _ = path[v + 1]
                my_list.append((src, dst, cost))
    Is_read = [False] * len(odd)
    sum_unread = 0
    sum_read = 0
    index_a = 0
    index_w = 0
    list_unread = []
    list_read = []
    for a, w, d in my_list:
        is_true = False
        for i in range(len(odd)):
            if a == odd[i]:
                index_a = i
                if Is_read[i]  == True:
                    is_true = True
            if w == odd[i]:
                index_w = i
                if Is_read[i] == True:
                    is_true = True
        if (is_true == True):
            sum_read += d
            list_read.append((a, w, d))
        else:
            sum_unread += d
            Is_read[index_a] = True
            Is_read[index_w] = True
            list_unread.append((a, w, d))
    if (sum_read < sum_unread):
        return list_read
    return list_unread

def eulerize(num_vertices, edges_list, is_oriented=False):
    """
    Update a undirected graph to an eulerian graph. It will modify the graph
    itself by adding edges.
    If the graph is already an eulerian graph. Nothing is updated.

    # TODO explain the algorithm
    :param is_oriented:
    :param num_vertices:
    :param edges_list:
    """
    
    if not is_oriented:
        '''
        For Cheick's version use that instead:

        odd = odd_vertices(num_vertices, edges_list, is_oriented)
        tmp = sort_odd(num_vertices, edges_list, odd, is_oriented)
        for i in range(len(tmp)):
        edges_list.append(tmp[i])
        '''
        odd = odd_vertices_undirected(num_vertices, edges_list)
        for i in range(0, len(odd) - 1, 2):
            first_vertex = odd[i]
            second_vertex = odd[i + 1]
            path = find_shortest_path(num_vertices, edges_list, first_vertex,
                                      second_vertex)
            # Create the new edges according to the path
            for v in range(0, len(path) - 1):
                src, cost = path[v]  # cost from src to dst
                dst, _ = path[v + 1]
                edges_list.append((src, dst, cost))
    else:
        M, succ = floyd_warshall(num_vertices, edges_list)
        f, set_pos, set_neg = find_feasible(num_vertices, edges_list)
        update_graph(edges_list, f, set_pos, set_neg, M, succ)
