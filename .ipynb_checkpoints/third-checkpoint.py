import algorithmx

# Create a Jupyter canvas interface
canvas = algorithmx.jupyter_canvas()

# Set the size of the canvas
canvas.size((300, 200))

# Use the library normally, for example:
canvas.nodes([1, 2]).add()
canvas.edge((1, 2)).add()

# Display the canvas
display(canvas)