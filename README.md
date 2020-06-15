# appero17
Exercice Recherche Operationelle - Optimisation des trajets des équipes de déneigement de la ville de Montréal

## Snowymontreal library

The snowymontreal module implements the solve function.

This function's signature is `solve(is_oriented, num_vertices, edges_list)` with
* is_oriented: is the graph oriented?
* num_vertices: The number of vertices.
* edges_list: the list of edges such as (**a**, **b**, **w**) is an edge (oriented or not) between **a** and **b** and its weight (cost) is **w**

Returns the most optimized (less costly) path such as every edges of the graph have been visited at least once.
The path is a cycle. It starts and ends at the same vertex.

### Import

`import snowymontreal`

Then **solve** can be used this way: `snowymontreal.solve(...)`

## Members

* Cheick
* Arnaud
* Kenz
* Antoine
* ilan.guenet
