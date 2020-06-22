from benchit import BenchIt as bench
import argparse
import snowymontreal as sm
import graph


def solve_directed():
    graphs = []
    directed = True
    for i in (1, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250):
        num_vertices, edges_list = graph.generate_connected_undirected_graph(
            i, directed)
        graphs.append((num_vertices, edges_list))

    b = bench("directed")
    for num_vertices, edges_list in graphs:
        sm.solve(directed, num_vertices, edges_list)
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
    parser = argparse.ArgumentParser(description="Benchmark")
    parser.add_argument('-d', '--directed', action='store_true',
                        help='Bench directed graph')
    parser.add_argument('-u', '--undirected', action='store_true',
                        help='Bench undirected graph')

    args = parser.parse_args()
    if args.undirected:
        solve_undirected()

    if args.directed:
        solve_directed()
