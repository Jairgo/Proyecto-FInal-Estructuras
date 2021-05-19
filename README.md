# Proyecto-FInal-Estructuras

#Comandos a instalar 
#Algorithmx
python -m pip install algorithmx
#HTTP Server
from algorithmx import http_server

# Create a new HTTP server on port 5050
server = http_server(port=5050)
# Create a new canvas
canvas = server.canvas()

def start():
    # Use the library normally, for example:
    canvas.nodes([1, 2]).add()
    canvas.edge((1, 2)).add()

    canvas.pause(1)

    canvas.node(1).highlight().size('1.5x').pause(0.5)
    canvas.edge((1, 2)).traverse('blue')

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()
