import algorithmx
from algorithmx import http_server
###
import networkx as nx
import os
# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()


    
lista = []
def start():
    #canvas.nodes(range(5)).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    #canvas.edges([(0, 1), (1, 2), (2, 3), (3, 4)]).add(directed=True)
    
    m = 1
    x = 0
    j=int(input("Digita el tamaño de lista: "))

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
    salir = False
    while not salir:
        os.system('cls')
        print("Ahora recargue la pagina y da click en play")
        print("El tamaño de la lista es: "+str(l))
        print("********* MENÚ *********")
        print("1.-Insertar al inicio")
        print("2.-Insertar al final")
        print("3.-Eliminar nodo en posición")
        print("4.-Agregar nodo en cierta posicion")
        print("5.-Salir")
        a = int(input("Que deseas hacer: "))

        if a == 1:
            val = int(input("Ingresa valor: "))
            insertBeg(val)
            
        elif a == 2:
            val = int(input("Ingresa valor: "))
            insertEnd(val)
            
        elif a == 3:
            val = int(input("Ingresa posicion a eliminar: "))
            eliminarNodo(val)
            
        elif a == 4:
            pos, val = [int(x) for x in input("Ingresa posicion y valor a agregar: ").split()]
            insertarNodo(pos,val)
        elif a==5:
            salir = True
    
    print ("Fin")

       

    

def insertBeg(val):
    canvas.node(val).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    lista.insert(0,val)
    x = lista[0]
    y = lista[1]
    canvas.edge((x,y)).add( directed = True )

def insertEnd(val):
    canvas.node(val).add(color='green',shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    canvas.pause(2.5)
    canvas.node(val).color('#323232')
    lista.append(val)
    tam = len(lista)
    x = lista[tam-2]
    y = lista[tam-1]
    canvas.edge((x,y)).add( directed = True )
    

def eliminarNodo(val):
    temp = lista[val]
    x = lista[val-1]
    y = lista[val+1]
    canvas.edge((x,temp)).remove()
    canvas.edge((temp,y)).remove()
    #canvas.node(temp).remove()
    canvas.node(temp).color('red').pause(2.5).remove().pause(2)
    canvas.edge((x,y)).add( directed = True )
    lista.remove(temp)

def insertarNodo(pos,val):
    canvas.node(val).add(shape='rect',size=(20, 20),pos=lambda n, i: ((i - 2) * 50, 20))
    tempX = lista[pos]
    tempY = lista[pos+1]
    canvas.edge((tempX,tempY)).remove()
    lista.insert(pos+1,val)
    tempX = lista[pos]
    tempY = lista[pos+1]
    canvas.edge((tempX,tempY)).add( directed = True )
    tempX = lista[pos+1]
    tempY = lista[pos+2]
    canvas.edge((tempX,tempY)).add( directed = True )
    
            

    

 
#start()

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()