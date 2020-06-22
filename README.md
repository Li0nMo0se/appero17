# appero17
Exercice Recherche Operationelle - Optimisation des trajets des équipes de déneigement de la ville de Montréal

## Snowymontreal library

The snowymontreal module implements the solve function.

This function's signature is `solve(is_oriented, num_vertices, edges_list)` with
* is_oriented: is the graph oriented?
* num_vertices: the number of vertices.
* edges_list: the list of edges such as (**a**, **b**, **w**) is an edge (oriented or not) between **a** and **b** and its weight (cost) is **w**

Returns the most optimized (less costly) path such as every edges of the graph have been visited at least once.
The path is a cycle. It starts and ends at the same vertex.

**Warning:** The given graph must be (strongly) connected.

### Import

`import snowymontreal`

Then **solve** can be used this way: `snowymontreal.solve(...)`

In addition, we allow people to use the auxiliary functions. The corresponding functions can be found in **snowymontreal.solve_aux**

`import snowymontreal.solve_aux`

You can find function such as:
* `eulerize(num_vertices, edges_list, is_oriented=False)`
* `is_valid(num_vertices, edges_list, is_oriented, path)`
* `is_eulerian(num_vertices, edges_list, is_oriented=False)`
* `is_eulerian_cycle(num_vertices, edges_list, is_oriented, cycle)`
* `find_eulerian_cycle(num_vertices, edges_list, is_oriented=False)`
* `is_connected(n, edges, is_oriented=False)`
* `find_shortest_path(num_vertices, edges_list, src, dst, is_oriented=False)`
* `floyd_warshall(num_vertices, edges_list)`


## Implementation

### Solve
    
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
    operation eulerize the graph

3) Third implementation:
    Now, we want to use the weights to minimize the cost. Also, weights 
    corresponds to a distance between two intersection. And a distance is 
    always positive. So, the weights are also always positive. We won't
    encounter negative cycles.
    We try to be smarter in the way we create the additional edges by
    minimizing the cost of the created edges.

4) Fourth implementation:
    We have been taking care of the drone with an undirected graph. In 
    this new iteration, we want to find a path for the plow. This
    time, the vehicles must follow the direction of the streets. Thus, 
    we use an oriented graph. Similarly, we eulerize an oriented graph.
    The algorithm to do so in quite different as for the non-oriented graph.

### Tests

Many unit tests are made (in the file eulerian_tests.py). It tests every 
auxiliary function needed by `solve`. By this way, it is easy to improve 
the program by iterations.

## Extra

### Installation

To use those extra features, you must install some dependencies with pip3
```bash
pip3 install -r requirements.txt
```

### Benchmark

A benchmark has been implemented to test the speed of our program. The script
 is located in `bench.py`.

```bash
usage: bench.py [-h] [-d] [-u]

optional arguments:
  -h, --help        show this help message and exit
  -d, --directed    Bench directed graph
  -u, --undirected  Bench undirected graph
```

It runs the `solve` function with randomly generated graphs. These graphs
respect the constraint of (strongly) connected. Basically, the script
generates graphs with a specific number of vertices that increase by 50
until reaching 250. It creates two sets of graph. The first set is for
undirected graphs. On the ohter hand, the second one is for directed graph.
By this way, it computes the time it takes to solve each graph and pretty
print it at the end.
    
### Interface with osmnx

Osmnx allows users to get graphs from cities. Hence, graphs can be downloaded
with osmnx. Then, with a cast, we can call solve with the downloaded graph.

Users can use our `solve` function with real cities which makes our solution
 useful in practice.
 
```bash
usage: solve with osmnx [-h] -c CITY [-d] [-u]

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  name of the city
  -d, --directed        solve for a directed graph
  -u, --undirected      solve for a undirected graph
```
 
**Warning:** for directed graph case, osmnx usually does not return a strongly
connected graph. As a reminder, `solve` can only be called with strongly
connected graphs. Thus, a assert will fail in most of the directed graph cases.

### Graph miscellaneous

In `graph.py`, some miscellaneous functions can be found.

* `generate_connected_undirected_graph(num_vertices, directed=False)`
* `print_graph(num_vertices, edges_list, is_oriented=False, name="graph")`
* `save_graph(num_vertices, filename, edges_list, is_oriented=False, name
="graph")`
* `to_reg_graph(osmnx_graph, is_oriented=False)`

## Members

* cheick-tidiane.dia
* arnaud.lassartesse
* kenz.narainen
* antoine.claudel
* ilan.guenet
