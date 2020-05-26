import osmnx as ox

if __name__ == '__main__':
    G = ox.graph_from_place('Montreal, Canada', network_type='drive')
    fig, ax = ox.plot_graph(G)
