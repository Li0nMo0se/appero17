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

### Import

`import snowymontreal`

Then **solve** can be used this way: `snowymontreal.solve(...)`

## Members

* cheick-tidiane.dia
* arnaud.lassartesse
* kenz.narainen
* antoine.claudel
* ilan.guenet

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
