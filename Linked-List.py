import algorithmx
from algorithmx import http_server
###
import networkx as nx

# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()


m = 1
x = 0
j=int(input("Digita el tamaño de lista: "))
lista = []
while j:
    x=int(input("Digita el "+str(m) + " valor: "))
    lista.append(x)
    canvas.node(x).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    x+=1
    m+=1
    j-=1

l = len(lista)
i=0
while i < l-1:
    x = lista[i]
    y = lista[i+1]
    canvas.edge((x,y)).add( directed = True )
    i+=1
print("Ahora recargue la pagina y da click en play")
    

def start():
    #canvas.nodes(range(5)).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    #canvas.edges([(0, 1), (1, 2), (2, 3), (3, 4)]).add(directed=True)
    print("El tamaño de la lista es: "+str(l))

        
            

    

 
#start()

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()