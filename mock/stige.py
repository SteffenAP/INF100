from uib_inf100_graphics import *

steps = 10

def redraw_all(app, canvas):
    canvas.create_line(app.width*0.3, app.height * 0, app.width * 0.3, app.height, fill = "red", width = 3)
    canvas.create_line(app.width*0.7, app.height * 0, app.width * 0.7, app.height, fill = "red", width = 3)
    for i in range(steps):
        canvas.create_line(app.width*0.3, (app.height * ((i)/steps) + 3), app.width * 0.7, (app.height * ((i)/steps) + 3), fill = "red", width = 3)

run_app(width = 600, height = 400)