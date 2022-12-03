from uib_inf100_graphics import *

TEXT = ' ,    ,\n{o,o}\n./)_)\n  " "    \n\nHello, Graphics!'

def redraw_all(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text=TEXT)

run_app(width=400, height=200)
