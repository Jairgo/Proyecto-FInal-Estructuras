import algorithmx
from algorithmx import http_server
###
import networkx as nx

import random
from random import randint

random.seed(436)


server = http_server(port=5050)
canvas = server.canvas()
canvas.size((500, 400))
def start():


    # Generate a random graph with random edge weights
    G = nx.newman_watts_strogatz_graph(16, 2, 0.4, seed=537)
    nx.set_edge_attributes(G, {e: randint(1, 20) for e in G.edges}, 'weight')

    # Add nodes and edges with weight labels
    canvas.nodes(G.nodes).add()
    canvas.edges(G.edges).add(
        labels=lambda e: {0: {'text': G.edges[e]['weight']}}
    )
    canvas.pause(1)

    # Select the source and target
    source = 0
    target = 8
    canvas.node(source).color('green').highlight().size('1.25x')
    canvas.node(target).color('red').highlight().size('1.25x')
    canvas.pause(1.5)

    # Run Dijkstra's shortest path algorithm
    path = nx.dijkstra_path(G, source, target)

    # Animate the algorithm
    path_length = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]

        # Update the path length
        path_length += G[u][v]['weight']

        # Traverse the edge
        canvas.edge((u, v)).traverse('blue')
        canvas.pause(0.4)

        # Make the next node blue
        if v != target:
            canvas.node(v).color('blue')

        # Add a label to indicate current path length
        canvas.node(v).label('path').add(
            color='blue',
            text=path_length
        )
        canvas.pause(0.4)

start()
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()