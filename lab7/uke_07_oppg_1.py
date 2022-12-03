from uib_inf100_graphics import *

def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    """ Tegner et rutenett med farger. Rutenettet er avgrenset av (x1, y1)
    i hjørnet til venstre oppe, og av (x2, y2) til høyre nede. Listen
    color_grid er en 2D-liste med strenger som representerer farger."""
    for row in range(len(color_grid)):# For hver rad, gjør følgende for hver kolonne i raden
        for col in range(len(color_grid[0])):
            canvas.create_rectangle((x1 + ((x2 - x1) * ((col)/(len(color_grid[0]))))), (y1 + ((y2 - y1) * ((row)/(len(color_grid))))) ,
                                    (x1 + ((x2 - x1) * ((col + 1)/(len(color_grid[0]))))), ((y1 + ((y2 - y1) * ((row + 1)/(len(color_grid)))))), 
                                    fill= color_grid[row][col])

def redraw_all(app, canvas):
    # Et 3x3 rutenett med innebygde farger
    draw_grid(canvas, 50, 20, 130, 100, [
        ["red", "green", "blue"],
        ["yellow", "pink", "cyan"],
        ["black", "gray", "orange"],
    ])

    # Et sjakkbrett
    draw_grid(canvas, 150, 20, 350, 100, [
        ["white", "black"] * 4,
        ["black", "white"] * 4,
    ] * 4)

    # En 2D-liste med kun én rad
    draw_grid(canvas, 50, 120, 350, 180, [
        ['#00c', '#01c', '#02c', '#03c', '#04c', '#05c', '#06c', '#07c',
         '#08c', '#09c', '#0ac', '#0bc', '#0cc', '#0dc', '#0ec', '#0fc']
    ])

run_app(width=400, height=200)