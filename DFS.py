## Ejemplo 1 = https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Salida 2 0 1 3

## Ejemplo 2 = http://myitlearnings.com/depth-first-search-dfs-for-traversing-a-graph/
# Salida 1 2 4 5 6 3

## Ejemplo 3 = https://algocoding.wordpress.com/2014/08/25/depth-first-search-java-and-python-implementation/
# Salida 0 1 5 6 4 2 3
import algorithmx
from algorithmx import http_server
###
import networkx as nx

G = nx.DiGraph()
paths = int(input("Ingrese la cantidad de edges: "))
while paths:
    x, y = [int(x) for x in input("Ingrese edge de U a V separados por un espacio: ").split()]
    nx.add_path(G, [x,y])
    paths-=1

inicio = int(input("ingrese el vertice de inicio: "))
print("Ahora abra la página y recargue")
"""
EJEMPLO 3 - 9 edges -inicio en 0
nx.add_path(G, [0,1])
nx.add_path(G, [0,2])
nx.add_path(G, [0,3])
nx.add_path(G, [1,5])
nx.add_path(G, [1,6])
nx.add_path(G, [2,4])
nx.add_path(G, [3,2])
nx.add_path(G, [3,4])
nx.add_path(G, [6,4])
"""
"""
EJEMPLO 2 - 6 edges - inicio en 1
nx.add_path(G, [1,2])
nx.add_path(G, [1,3])
nx.add_path(G, [2,4])
nx.add_path(G, [2,5])
nx.add_path(G, [3,6])
nx.add_path(G, [5,6])
"""
"""
EJEMPLO 1 - 6 edges - inicio en 2
nx.add_path(G, [0,1])
nx.add_path(G, [0,2])
nx.add_path(G, [1,2])
nx.add_path(G, [2,0])
nx.add_path(G, [2,3])
nx.add_path(G, [3,3])
"""





###
# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()
# Create a new canvas
###
texto = []
texto.append("Orden del recorrido: ")
texto.append(str(inicio))


def finished(str1):
    canvas.label('title').add(text=str1)

def start():
    nx.set_node_attributes(G, False, 'seen')
    canvas.nodes(G.nodes).add()
    canvas.edges(G.edges).add(directed=True)
    canvas.pause(1)
    print(inicio,end=" <- Inicio\n")


    dfs(inicio)

def dfs(n):
    G.nodes[n]['seen'] = True

    canvas.node(n).highlight().size('1.25x') # Hace grande el circulo
    canvas.node(n).color('blue')    # Colorea de azul el circulo
    canvas.pause(0.5) # Se espera medio segundo antes de seguir
    
    for n2 in G.neighbors(n):
        if G.nodes[n2]['seen']:
            continue

        canvas.edge((n, n2)).traverse('red').pause(0.5)
        print(n2)
        texto.append(str(n2))

        dfs(n2) # DFS on neighbor
        canvas.edge((n2, n)).traverse('blue').pause(0.5)
        canvas.node(n).highlight().size('1.25x').pause(0.5)

    str1 = ' '.join(texto)
    print(str1)
    finished(str1)






canvas.onmessage('finished', finished)
canvas.message('finished')


# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()