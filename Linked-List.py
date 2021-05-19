import algorithmx
from algorithmx import http_server
###
import networkx as nx

# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()

def start():
    canvas.nodes((1, 2)).add()
    canvas.pause(0.5)
    canvas.edge((1, 2)).add(directed=True)
    canvas.node(2).highlight().size('2.25x').pause(0.5) #Resalta el nodo
    canvas.edge((1, 2)).traverse('blue') #Dibuja linea en azul
    canvas.pause(0.5)
    canvas.nodes([3]).add()
    canvas.node(3).highlight().size('2.25x').pause(0.5) #Resalta el nodo
    canvas.edge((2, 3)).traverse('blue') #Dibuja linea en azul
    canvas.node(2).color('red').pause(1).remove().pause(1)
    canvas.edge((1, 3)).traverse('blue') #Dibuja linea en azul
    canvas

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()