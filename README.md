# Proyecto-FInal-Estructuras

#Comandos a instalar 

python -m pip install algorithmx

from algorithmx import http_server
server = http_server(port=5050)
canvas = server.canvas()
def start():
    # Use the library normally, for example:
    canvas.nodes([1, 2]).add()
    canvas.edge((1, 2)).add()

   
canvas.onmessage('start', start)
server.start()
