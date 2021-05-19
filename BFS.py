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
"""
print("¿Cuántos nodos tiene el grafo?")
n = int(input()) # 4 para este ejemplo
i = 0

while i < n:
  G.add_node(i)
  i+=1
  #G.add_nodes_from([0, 1, 2, 3])
"""

print("¿Cuántos edges tiene el grafo?")
n = int(input()) # 5 para este ejemplo

while n:
  x, y = [int(x) for x in input("Ingrese edge de U a V separados por un espacio: ").split()]
  nx.add_path(G, [x,y])
  #G.add_edge(x,y)
  n-=1
print("Los nodos de este grafo: " + str(list(G.nodes)) +"\n")
inicio = int(input("Ingresa el vertice inicio: ")) # 2 para este ejemplo
print("Ahora recarge la pagina y de clik en iniciar \n")
"""
#print(list(G.nodes))
G.add_nodes_from([0, 1, 2, 3])
G.add_edges_from([(0, 1), (0, 2), (1, 2), (2,0), (2,3)])
#print(G.size())

"""
###
# Create a new HTTP server on port 5050
server = http_server(port=5050)

# Create a new canvas
canvas = server.canvas()
###

def start():
    canvas.nodes(G.nodes).add()
    canvas.edges(G.edges).add(directed=True)
    canvas.pause(1)
    bfs(inicio)
    

def bfs(n):
    texto = []
    texto.append("Orden del recorrido: ")
    visited = [False] * 100;
    #visited = [False] * (max(G.size()) + 1)
    queue = []

    queue.append(n)
    visited[n] = True

    while queue:
      n = queue.pop(0)
      texto.append(str(n))

      for n2 in G.neighbors(n):
          if visited[n2] == False:
              colorear(n,n2)
              queue.append(n2)
              visited[n2] = True
              G.nodes[n2]['seen'] = True
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