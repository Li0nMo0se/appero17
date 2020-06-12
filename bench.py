from benchit import BenchIt as bench
import snowymontreal as sm
import graph
import sys


def solve_directed():
    graphs = []
    directed = True
    for i in (1, 25, 50, 75, 100, 125, 150, 175, 200):
        num_vertices, edges_list = graph.generate_connected_undirected_graph(
            i, directed)
        graphs.append((num_vertices, edges_list))

    b = bench("directed")
    for num_vertices, edges_list in graphs:
        path = sm.solve(directed, num_vertices, edges_list)
        b(f"{num_vertices} vertices, {len(edges_list)} edges")
    b.stop()
    b.display()


def solve_undirected():
    graphs = []
    directed = False
    for i in (1, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250):
        num_vertices, edges_list = graph.generate_connected_undirected_graph(i)
        graphs.append((num_vertices, edges_list))

    b = bench("undirected")
    for num_vertices, edges_list in graphs:
        sm.solve(directed, num_vertices, edges_list)
        b(f"{num_vertices} vertices, {len(edges_list)} edges")
    b.stop()
    b.display()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(f"Usage: python3 {sys.argv[0]} [benchmark name]",
              file=sys.stderr)
    else:
        # solve_undirected()
        solve_directed()
