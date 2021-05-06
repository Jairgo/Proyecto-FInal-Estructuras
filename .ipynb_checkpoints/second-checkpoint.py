import networkx as nx
from algorithmx import jupyter_canvas
from algorithmx import http_server

G = nx.Graph()

nx.add_path(G, [1, 2, 3])
nx.add_path(G, [4, 2, 5])

print('Nodes:', G.nodes)
print('Edges:', G.edges)

server = http_server(port=5052)
canvas = jupyter_canvas()

canvas.nodes(G.nodes).add()
canvas.edges(G.edges).add()

server.start()