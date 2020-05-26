# library solve

'''
        Contain some functions needed by solve.py
'''

def nedge(a, b):
    return (a, b) if a < b else (b, a)


def is_eulerian_cycle(n, edges, cycle):
    if len(edges) != len(cycle):
        return False
    if len(edges) == 0:
        return True
    eset = {}
    for (a, b) in edges:
        s = nedge(a, b)
        if s in eset:
            eset[s] += 1
        else:
            eset[s] = 1
    for (a, b) in zip(cycle, cycle[1:]+cycle[0:1]):
        s = nedge(a, b)
        if s in eset and eset[s] > 0:
            eset[s] -= 1
        else:
            return False
    for val in eset.values():
        if val != 0:
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

def adjacency_list(num_vertices, edges_list, is_oriented=False):
    succ = [[] for _ in range(num_vertices)]
    for (a, b, _) in edges_list:
        succ[a].append(b)
        if not is_oriented:
            succ[b].append(a)
    return succ


def odd_vertices(n, edges):
    deg = [0] * n
    for (a,b) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]
