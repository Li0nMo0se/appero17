import osmnx as ox
import snowymontreal as nm
import graph
import snowymontreal.solve_aux as sa
from benchit import BenchIt as bench
import argparse

"""
    Use solve with osmnx.
    Give the name of the city in argument and whether the problem has to be 
    solved with a directed or undirected graph
    First, parse the arguments. Secondly, download the graph. Finally, 
    call solve on the graph that is previsously casted to comply with our 
    implementation.
    Warning: The graph must be edges connected
"""


parser = argparse.ArgumentParser('solve with osmnx')

parser.add_argument('-c', '--city', type=str, help='name of the city',
                    required=True)
parser.add_argument('-d', '--directed', action='store_true',
                    help='solve for a directed graph')
parser.add_argument('-u', '--undirected', action='store_true',
                    help='solve for a undirected graph')

args = parser.parse_args()

is_oriented = False
if args.directed:
    is_oriented = True
elif args.undirected:
    is_oriented = False

city = args.city

G = ox.graph_from_place(city, network_type='drive',
                        simplify=True)
G = ox.add_edge_bearings(G)
num_vertices, edges_list = graph.to_reg_graph(G, is_oriented)

print(f"city: {city}, oriented: {is_oriented}")
print(f"number of vertices: {num_vertices}")
print(f"number of edges: {len(edges_list)}")
assert(sa.is_edge_connected(num_vertices, edges_list, is_oriented))
b = bench(city)
b(city)
path = nm.solve(is_oriented, num_vertices, edges_list)
b.stop()
print("time: ", "{0:.5f}".format(b.times[city][0]), "s", sep='')
print(f"solved: {sa.is_valid(num_vertices, edges_list, is_oriented, path)}")
