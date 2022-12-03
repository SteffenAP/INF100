from uib_inf100_graphics import *

def app_started(app):
    app.redval = 0
    app.greenval = 0
    app.blueval = 0
    app.hex = "#000000"

def rgb_hexstring(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def key_pressed(app, event):
    if event.key == "Up":
        if app.redval < 255:
            app.redval += 1
            app.hex = rgb_hexstring(app.redval, app.greenval, app.blueval)
    if event.key == "Down":
        if app.redval > 0:
            app.redval -= 1
            app.hex = rgb_hexstring(app.redval, app.greenval, app.blueval)
    if event.key == "Right":
        if app.greenval < 255:
            app.greenval += 1
            app.hex = rgb_hexstring(app.redval, app.greenval, app.blueval)
    if event.key == "Left":
        if app.greenval > 0:
            app.greenval -= 1
            app.hex = rgb_hexstring(app.redval, app.greenval, app.blueval)
    if event.key == "a":
        if app.blueval < 255:
            app.blueval += 1
            app.hex = rgb_hexstring(app.redval, app.greenval, app.blueval)
    if event.key == "z":
        if app.blueval > 0:
            app.blueval -= 1
            app.hex = rgb_hexstring(app.redval, app.greenval, app.blueval)

        
def redraw_all(app, canvas):
    canvas.create_text(app.width * 0.5, app.height * 0.1,  text = "Trykk på piltastene eller a/z for å endre fargen")
    canvas.create_oval(app.width * 0.25, app.height * 0.25, app.width * 0.75, app.height * 0.75, fill = app.hex)

run_app(width = 600, height = 400, title = "color")   