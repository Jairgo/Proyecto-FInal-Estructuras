import algorithmx
from algorithmx import http_server
###
import networkx as nx

canvas = algorithmx.jupyter_canvas(buttons=True)
canvas.size((300, 200))

canvas.nodes([1, 2]).add()
canvas.edge((1, 2)).add()

canvas.pause(0.5)

canvas.node(1).highlight().size('1.25x').pause(0.5)
canvas.edge((1, 2)).traverse('blue')

canvas