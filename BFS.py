## Ejemplo sacado de https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
## Salida: 2 0 3 1
import algorithmx
from algorithmx import http_server
###
import networkx as nx

G = nx.Graph()
#G = nx.fast_gnp_random_graph(10, 0.3, seed=50)
#G.add_edge("a", "b", weight=7)

nx.add_path(G, [0,1])
nx.add_path(G, [0,3])
nx.add_path(G, [1,0])
nx.add_path(G, [1,2])
nx.add_path(G, [2,1])
nx.add_path(G, [2,3])
nx.add_path(G, [3,0])
nx.add_path(G, [3,2])

#nx.add_path(G, [1,3])


nx.set_node_attributes(G, False, 'seen')


###
# Create a new HTTP server on port 5050
#server = http_server(port=5050)
#canvas = server.canvas()
# Create a new canvas
###

def start():
    #canvas.nodes(G.nodes).add()
    #canvas.edges(G.edges).add()
    #canvas.pause(1)
    bfs(0)

def bfs(n):
    queue = []
    queue.append(n)
    G.nodes[n]['seen'] = True

    while queue:
      n = queue.pop(0)
      print(n, end = " ")

        #canvas.node(n).highlight().size('1.25x') # Hace grande el circulo
        #canvas.node(n).color('blue')    # Colorea de azul el circulo
        #canvas.pause(0.5) # Se espera medio segundo antes de seguir

      for n2 in G.neighbors(n):
          if G.nodes[n2]['seen'] == False:
              queue.append(n2)
              G.nodes[n2]['seen'] = True
                #continue

            #canvas.edge((n, n2)).traverse('red').pause(0.5)
            #bfs(n2) # DFS on neighbor
            #canvas.edge((n2, n)).traverse('blue').pause(0.5)
            #canvas.node(n).highlight().size('1.25x').pause(0.5)

start()
# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
#canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
#server.start()