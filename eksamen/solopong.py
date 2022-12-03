from uib_inf100_graphics import *

def app_started(app):
    app.racket_x, app.racket_y = (app.width * 0.95, app.height * 0.5) #racketkjerne
    app.racket_height = app.height * 0.2 #rackethøyde
    app.circle_left = app.width//2
    app.circle_top = app.height//2
    app.circle_size = 25
    app.dx = -4
    app.dy = 5
    app.is_paused = False
    app.timer_delay = 25 # millisekunder
    app.state = "active" #active/gameover

def key_pressed(app, event):
    if event.key == "p" and app.state == "active":
        app.is_paused = not app.is_paused
    if event.key == "s" and app.state == "active":
        do_step(app)
    if event.key == "Up" and app.state == "active":
        move_racket_up(app)
    if event.key == "Down" and app.state == "active":
        move_racket_down(app)

def timer_fired(app):
    if not app.is_paused and app.state == "active":
        do_step(app)

def move_racket_up(app):
    if ((app.racket_y - 5)- app.racket_height) <= 0:
        app.racket_y = (0 + app.racket_height)
    else:
        app.racket_y -= 5

def move_racket_down(app):
    if ((app.racket_y + 5) + app.racket_height)  >= app.height:
        app.racket_y = (app.height - app.racket_height)
    else:
        app.racket_y += 5

def bounce_detection(app): #sjekker for kollisjon
    if app.circle_left >= app.racket_x - app.circle_size:
        if ((app.racket_y - app.racket_height <= app.circle_top <= app.racket_y + app.racket_height) or (app.racket_y - app.racket_height <= app.circle_top + app.circle_size <= app.racket_y + app.racket_height)) == True:
            app.circle_left = app.racket_x - app.circle_size
            app.dx = -app.dx  


def do_step(app):
    bounce_detection(app)
    # Flytt horisontalt
    app.circle_left += app.dx

    # Sjekk om firkanten har gått utenfor lerretet, og hvis ja, snu
    # retning; men flytt også firkanten til kanten (i stedet for å gå
    # forbi). Merk: det finnes andre, mer sofistikerte måter å håndtere
    # at rektangelet går forbi kanten...
    if app.circle_left < 0:
        # snu retningen!
        app.circle_left = 0
        app.dx = -app.dx
    elif app.circle_left > app.width - app.circle_size:
        app.circle_left = app.width - app.circle_size
        app.state = "gameover" #hvis den treffer vegg gameover
        return
    
    # Flytt vertikalt på samme måte
    app.circle_top += app.dy
    if app.circle_top < 0:
        # snu retningen!
        app.circle_top = 0
        app.dy = -app.dy
    elif app.circle_top > app.height - app.circle_size:
        app.circle_top = app.height - app.circle_size
        app.dy = -app.dy

def redraw_all(app, canvas):
    # tegn firkanten
    canvas.create_oval(
        app.circle_left,
        app.circle_top,
        app.circle_left + app.circle_size,
        app.circle_top + app.circle_size,
        fill="yellow",)
    canvas.create_rectangle(
        (app.racket_x - 5),
        (app.racket_y - app.racket_height),
        (app.racket_x + 5),
        (app.racket_y + app.racket_height),
        fill="black"
    )
    
    # tegn teksten
    canvas.create_text(
        app.width/2, 20,
        text="Trykk 'p' for å sette på pause",
    )
    canvas.create_text(
        app.width/2, 40,
        text="Trykk 's' for å gjør et enkelt steg",
    )
    if app.state == "gameover":
            canvas.create_text(
        app.width/2, 80,
        text="GAMEOVER",
    )

run_app(width=400, height=150)