## Ejemplo sacado de https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
## Salida: 2 0 3 1
import algorithmx
from algorithmx import http_server
###
import networkx as nx

G = nx.DiGraph()
#G = nx.fast_gnp_random_graph(10, 0.3, seed=50)
#G.add_edge("a", "b", weight=7)
"""
nx.add_edge(G)


nx.add_path(G, [0,1])
nx.add_path(G, [0,2])
nx.add_path(G, [1,2])
nx.add_path(G, [2,0])
nx.add_path(G, [2,3])
nx.add_path(G, [3,3])

#nx.add_path(G, [1,3])
"""




#nx.set_node_attributes(G, False, 'seen')

G.add_nodes_from([0,1, 2, 3])
#G.add_edges_from([(1, 2), (2, 3), (3, 1)])
G.add_edges_from([(0, 1), (0, 2), (1, 2), (2,0), (2,3)])
print(G.size())
###
# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()
# Create a new canvas
###

def start():
    canvas.nodes(G.nodes).add()
    canvas.edges(G.edges).add(directed=True)
    canvas.pause(1)
    bfs(2)
    

def bfs(n):
    texto = []
    texto.append("Orden del recorrido: ")
    visited = [False] * 100;
    #visited = [False] * (max(G.size()) + 1)
    queue = []

    queue.append(n)
    visited[n] = True
    #G.nodes[n]['seen'] = True

    while queue:
      n = queue.pop(0)
      #print(n," ")
      texto.append(str(n))
      #print (texto)

      #canvas.node(n).highlight().size('1.25x') # Hace grande el circulo
      #canvas.node(n).color('blue')    # Colorea de azul el circulo
      #canvas.pause(0.5) # Se espera medio segundo antes de seguir
      #canvas.edge((0, 1)).traverse('red')
      for n2 in G.neighbors(n):
          if visited[n2] == False:
          #if G.nodes[n2]['seen'] == False:
              colorear(n,n2)
              queue.append(n2)
              G.nodes[n2]['seen'] = True
                #continue
              #print(n2 ," ")
              #print("va de ", n ," a " , n2)
              
            #bfs(n2) # DFS on neighbor
            ##canvas.edge((n2, n)).traverse('blue').pause(0.5)
            ##canvas.node(n).highlight().size('1.25x').pause(0.5)
    str1 = ' '.join(texto)
    finished(str1)


def colorear(n,n2):
    canvas.node(n).highlight().size('1.25x') # Hace grande el circulo
    canvas.node(n).color('blue')    # Colorea de azul el circulo
    canvas.pause(0.5) # Se espera medio segundo antes de seguir
    canvas.edge((n, n2)).traverse('red')
    canvas.node(n2).highlight().size('1.25x') # Hace grande el circulo
    canvas.node(n2).color('blue')    # Colorea de azul el circulo
    canvas.pause(0.5)
    
def finished(str1):
    string = str1
    canvas.label('title').add(text=string)

canvas.onmessage('finished', finished)
canvas.message('finished')

start()
# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()