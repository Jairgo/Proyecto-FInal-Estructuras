import algorithmx
from algorithmx import http_server

# Create a new HTTP server on port 5050
server = http_server(port=5050)
# Create a new canvas
canvas = server.canvas()

def start():
    canvas.nodes(range(1, 8)).add()
    canvas.edges([(i, i+1) for i in range(1, 7)]
           + [(1, 3), (2, 4), (2, 7)]).add()

    for i in range(1, 8):
        canvas.pause(0.5)
        canvas.node(i).color('green').highlight().size('1.25x')
        
        if i < 7:
            canvas.pause(0.5)
            canvas.edge((i, i+1)).traverse('green')

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()