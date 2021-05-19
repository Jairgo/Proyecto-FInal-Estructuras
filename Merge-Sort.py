# Merge Sort
import algorithmx
from algorithmx import http_server
###
import networkx as nx
import math
# Create a new HTTP server on port 5050
server = http_server(port=5050)
canvas = server.canvas()
#  unsorted = [17, 13, 12, 16, 18, 15, 11, 14]
j=1
unsorted= []
numero = int(input("Introduce tamaño del arreglo:" ))
for i in range(numero): 
    n = int(input("Introduce el numero " + str(j) + " : " ))
    unsorted.append(n)
    j+=1
print("Recarga la pagina y dale play")
def start():
    def node_pos(i, level):
        x = (i - (len(unsorted) - 1) / 2) * 80
        y = -(level - math.ceil(math.log2(len(unsorted))) / 2) * 120
        return (x, y)

    def node_id(i, level):
        return str(i) + '_' + str(level)

    def animate_merge_edge(node_prev, node_cur, number, color):
        edge = (node_prev, node_cur)

        canvas.node(node_prev).color(color)
        canvas.edge(edge).add().directed(True)
        canvas.pause(0.5)

        canvas.edge(edge).duration(0.8).traverse(color).pause(0.2)
        canvas.node(node_cur).label().text(number).visible(True)
        canvas.pause(0.5)


    def animate_merge(left, right, index, level):
        total_len = len(left) + len(right)
        prev_ids = [node_id(index + i, level - 1) for i in range(total_len)]
        cur_ids = [node_id(index + i, level) for i in range(total_len)]

        canvas.nodes(cur_ids).add(
            shape='rect',
            size=(30, 15),
            fixed=True,
            pos=lambda _, i: node_pos(index + i, level),
            labels={0: {'visible': False }}
        )

        canvas.edges([(cur_ids[i], cur_ids[i + 1])
            for i in range(len(cur_ids) - 1)]).add()

        canvas.pause(0.8)

        li = 0
        ri = 0
        result = []
        for i in range(total_len):
            if ri == len(right) or (li < len(left) and left[li] < right[ri]):
                result.append(left[li])
                animate_merge_edge(prev_ids[li], cur_ids[i],
                    left[li], 'green')
                li += 1
            else:
                result.append(right[ri])
                animate_merge_edge(prev_ids[len(left) + ri], cur_ids[i],
                    right[ri], 'red')
                ri += 1

        return result

    def merge_sort(array, index=0, level=None):
        level = math.ceil(math.log2(len(array))) if level is None else level

        if len(array) == 1:
            if level != 0:
                animate_merge(array, [], index, level)
            return array

        split_index = len(array) // 2
        left = merge_sort(array[0:split_index], index, level - 1)
        right = merge_sort(array[split_index:], index + split_index, level - 1)

        return animate_merge(left, right, index, level)

    canvas.pause(0.1)
    top_ids = [node_id(i, 0) for i in range(len(unsorted))]

    canvas.nodes(top_ids).data(unsorted).add(
        shape='rect',
        size=(30, 15),
        fixed=True,
        pos=lambda _, i: node_pos(i, 0),
        labels=lambda n: {0: {'text': n }}
    )

    canvas.pause(1)
    merge_sort(unsorted)

# A 'start' message is sent by the client whenever the
# user clicks the start or restart button
canvas.onmessage('start', start)

# Start the server, blocking all further execution on
# the current thread. Use 'ctrl-c' to exit the script.
server.start()