from uib_inf100_graphics import *
import random

def app_started(app):
    app.rows = 5
    app.cols = 8
    app.margin = 0.1 * app.width
    app.mole = random_mole_location(app)
    app.points = 0
    app.hover = (-1, -1)

def point_in_grid(app, x, y):
    return ((app.margin <= x <= (app.width - app.margin)) and
            (app.margin <= y <= (app.height - app.margin)))

def get_cell(app, x, y):
    if (point_in_grid(app, x, y) == False):
        return (-1, -1)
    grid_width  = app.width - (2 * app.margin)
    grid_height = app.height - (2 * app.margin)
    cell_width  = (grid_width / app.cols)
    cell_height = (grid_height / app.rows)
    row = int((y - app.margin) / cell_height)
    col = int((x - app.margin) / cell_width)
    return (row, col)

def get_cell_bounds(app, row, col):
    grid_width  = app.width - (2 * app.margin)
    grid_height = app.height - (2 * app.margin)
    column_width = (grid_width / app.cols)
    row_height = (grid_height / app.rows)
    x0 = app.margin + (col * column_width)
    x1 = app.margin + ((col + 1) * column_width)
    y0 = app.margin + (row * row_height)
    y1 = app.margin + ((row + 1) * row_height)
    return (x0, y0, x1, y1)

def random_mole_location(app):
    new_location = (random.choice(range(app.rows)), random.choice(range(app.cols)))
    return new_location

def mouse_moved(app, event):
    app.hover = get_cell(app, event.x, event.y)
    

def mouse_pressed(app, event):
    app.click = get_cell(app, event.x, event.y)
    if app.mole == app.click:
        app.points += 1
        app.mole = (-1, -1)
        app.mole = random_mole_location(app)

def redraw_all(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = get_cell_bounds(app, row, col)
            if app.mole == (row, col) and app.hover == (row, col):
                fill = "light yellow"
            elif app.mole == (row, col):
                fill = "yellow"
            elif app.hover == (row, col):
                fill = "grey60"
            else:
                fill = "grey50"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    canvas.create_text(app.width/2, app.height * 0.1, text=f"Points: {app.points}",
                       font="Arial 15 bold", fill="black")

run_app(width=600, height=400)