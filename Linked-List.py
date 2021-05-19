import algorithmx
from algorithmx import http_server
###
import networkx as nx

# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()

    

def start():
    #canvas.nodes(range(5)).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    #canvas.edges([(0, 1), (1, 2), (2, 3), (3, 4)]).add(directed=True)
    """ canvas.node(0).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))


    canvas.node(1).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))


    canvas.node(2).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    canvas.node(3).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))


    canvas.edge((0,1)).add(directed=True)
    canvas.edge((1,2)).add(directed=True)
    canvas.edge((2,3)).add(directed=True)
    """
    m = 1
    x = 0
    j=int(input("Digita el tamaño de lista: "))
    o=j
    lista = []
    while j:
        x=int(input("Digita el "+str(m) + " valor: "))
        lista.append(x)
        canvas.node(x).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
        x+=1
        m+=1
        j-=1


    band = 0
    x=0
    for i in lista:
        if(band ==0):
            x = i
            band = 1
            break
        else:
            y=x+1
            band=0
            canvas.edge((x,y)).add(directed=True)
        
            

    

 
#start()

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()