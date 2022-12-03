import random
from uib_inf100_graphics import *
from uib_inf100_music import load_sound
import copy

def restart(app): #kjører spill på kall
    app.fleetimer = 0 #teller hvor lenge spillet har vært i "flee" modus
    app.timer = 0 #teller antall flytt, og når spøkelsene får lov til å gå
    app.state = "active" # variabel som sjekker active/gameover/complete
    app.prev_val_blinky = 0 # variabel som lagrer verdien den står på, slik at poeng ikke forsvinner, spøkelse blinky (rød)
    app.blinkyval = 2 #blinky sin verdi i board
    app.blinkyrow = 10 #blinky sin startrow
    app.blinkycol = 10 #blinky sin startcol

    app.prev_val_pinky = 0 #samme som over, bare for pinky (rosa)
    app.pinkyval = 3
    app.pinkyrow = 10
    app.pinkycol = 9

    app.prev_val_inky = 0 #samme som over, bare for inky (blå)
    app.inkyval = 4
    app.inkyrow = 10
    app.inkycol = 11

    app.prev_val_clyde = 0 #samme som over, bare for clyde (oransje)
    app.clydeval = 5
    app.clyderow = 10
    app.clydecol = 12

    app.head_pos = (4, 10) #Hvor pac-man starter
    app.new_pos = (4, 10) #Hvor pac man skal
    app.direction = "east" #Startretning pac-man
    app.board = [ #brett
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1],
    [1, -2, 1, 1, -2, 1, 1, 1, 1, -2, 1, -2, 1, 1, 1, 1, -2, 1, 1, -2, 1],
    [1, -2, 1, 1, -2, 1, 1, 1, 1, -2, 1, -2, 1, 1, 1, 1, -2, 1, 1, -2, 1],
    [1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1],
    [1, -2, 1, 1, -2, 1, -2, 1, 1, 1, 1, 1, 1, 1, -2, 1, -2, 1, 1, -2, 1],
    [1, -2, -2, -2, -2, 1, -2, -2, -2, -2, 1, -2, -2, -2, -2, 1, -2, -2, -2, -2, 1],
    [1, 1, 1, 1, -2, 1, 1, 1, 1, -2, 1, -2, 1, 1, 1, 1, -2, 1, 1, 1, 1],
    [1, 1, 1, 1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -2, 1, 1, 1, 1],
    [1, 1, 1, 1, -2, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, -2, 1, 1, 1, 1],
    [0, 0, 0, 0, -2, 0, 0, 1, 1, 3, 2, 4, 5, 1, 0, 0, -2, 0, 0, 0, 0],
    [1, 1, 1, 1, -2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, -2, 1, 1, 1, 1],
    [1, 1, 1, 1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -2, 1, 1, 1, 1],
    [1, 1, 1, 1, -2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, -2, 1, 1, 1, 1],
    [1, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1],
    [1, -2, 1, 1, -2, 1, 1, 1, 1, -2, 1, -2, 1, 1, 1, 1, -2, 1, 1, -2, 1],
    [1, -2, -2, 1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1, -2, -2, 1],
    [1, 1, -2, 1, -2, 1, -2, 1, 1, 1, 1, 1, 1, 1, -2, 1, -2, 1, -2, 1, 1],
    [1, -2, -2, -2, -2, 1, -2, -2, -2, -2, 1, -2, -2, -2, -2, 1, -2, -2, -2, -2, 1],
    [1, -2, 1, 1, 1, 1, 1, 1, 1, -2, 1, -2, 1, 1, 1, 1, 1, 1, 1, -2, 1],
    [1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]


def app_started(app): #bootup funksjon
    app.fleesound = load_sound("flee.mp3") #fruktmusikk
    app.fleesound.stop() #sørger for at den ikke starter av seg selv
    app.playstate = True #pause/resume
    app.debug_mode = True #Starter i debug
    app.fruitspawntimer = 0 #sjekker når frukt skal spawne
    app.state = "active" # active/gameover/complete
    app.ghoststate = "chase" #chase/flee for å sjekke om de kan spises
    app.timer_delay = 100 # tidsdelay for timer_fired
    app.points = 0 #poengteller
    restart(app) #kjører spill



def timer_fired(app):
    if app.debug_mode == False and app.playstate == True and app.state == "active": #Spiller kjører hvis debug av, spill igang og ikke pause,
        if (-2 in (item for sublist in app.board for item in sublist)) == False:
            app.state = "complete" #sjekker om det er poeng igjen på brettet
            return
        app.fruitspawntimer += 1                                                                             
        move_pacman(app) #flytter pacman
        app.timer += 1 #øker moves
        if app.timer >= 5: #rød ghost går ifra timer 5
            move_ghost_blinky(app)
        if app.timer >= 20: #rosa går ifra 20
            move_ghost_pinky(app)
        if app.timer >= 35: #blå går ifra 35
            move_ghost_inky(app)
        if app.timer >= 50: #oransj går ifra 50
            move_ghost_clyde(app)
        if app.fruitspawntimer == 100: # adder en frukt som kan spise spøkelser hvert 100de move
            add_superfruit_at_random_location(app.board, app)
        if app.ghoststate == "flee":
            app.fleetimer += 1 #teller for flee modus
        if app.fleetimer == 50: #frukt varer i 50 moves
            app.ghoststate = "chase" #spillet går tilbake til vanlig modus
            app.fleesound.stop() #musikken stopper
            app.fleetimer = 0 #timer resettes

def key_pressed(app, event):
    if event.key == "d": #debug toggle
        app.debug_mode = not app.debug_mode
    if event.key == "p": #pause toggle
        app.playstate = not app.playstate
    if app.playstate == True: #Hvis spill i gang og ikke på pause
        if event.key == "Up":# gå opp
            app.direction = "north"
        if event.key == "Down": # gå ned
            app.direction = "south"
        if event.key == "Right": # gå høyre
            app.direction = "east"
        if event.key == "Left": #gå venstre
            app.direction = "west"
    if app.debug_mode == True: # gå med space i debug, samme som timer fired, men trigges bare ved space
        if event.key == "Space":
            if (-2 in (item for sublist in app.board for item in sublist)) == False:
                app.state = "complete" #sjekker om det er poeng igjen på brettet
                return
            app.fruitspawntimer += 1                                                                                  
            move_pacman(app) #flytter pacman
            app.timer += 1 #øker moves
            if app.timer >= 5: #rød ghost går ifra timer 5
                move_ghost_blinky(app)
            if app.timer >= 20: #rosa går ifra 20
                move_ghost_pinky(app)
            if app.timer >= 35: #blå går ifra 35
                move_ghost_inky(app)
            if app.timer >= 50: #oransj går ifra 50
                move_ghost_clyde(app)
            if app.fruitspawntimer == 100: # adder en frukt som kan spise spøkelser hvert 100de move
                add_superfruit_at_random_location(app.board, app)
            if app.ghoststate == "flee":
                app.fleetimer += 1 #teller for flee modus
            if app.fleetimer == 50: #frukt varer i 50 moves
                app.ghoststate = "chase" #spillet går tilbake til vanlig modus
                app.fleesound.stop() #musikken stopper
                app.fleetimer = 0 #timer resettes
    if app.state == "gameover": #sjekker game over
        if event.key == "Enter": #restart
            app.points = 0 #setter poeng til 0
            restart(app)
    if app.state == "complete": #samme som over, men poeng fører over
        if event.key == "Enter":
            restart(app)



def draw_board(canvas, x1, y1, x2, y2, board, debug_mode, app):
        colorboard = copy.deepcopy(board) # kopierer brettet for å finne farger
        for row in range(len(board)):# For hver rad, gjør følgende for hver kolonne i raden
            for col in range(len(board[0])):
                if board[row][col] == -1: #Pac-Man
                    colorboard[row][col] = "#FFFF00"
                if board[row][col] == 0: #Bakke
                    colorboard[row][col] = "black"
                if board[row][col] == 1: #Vegg
                    colorboard[row][col] = "#1919A6"
                if board[row][col] == -2: #Points
                    colorboard[row][col] = "black"
                if board[row][col] == -3: #Superfrukt
                    colorboard[row][col] = "purple"
                if board[row][col] == 2: #Spøkelse Blinky
                    colorboard[row][col] = "#FF0000"
                if board[row][col] == 3: #Spøkelse Pinky
                    colorboard[row][col] = "#FFB8FF"
                if board[row][col] == 4: #Spøkelse Inky
                    colorboard[row][col] = "#00FFFF"
                if board[row][col] == 5: #Spøkelse Clyde
                    colorboard[row][col] = "#FFB852"
                canvas.create_rectangle((x1 + ((x2 - x1) * ((col)/(len(board[0]))))), (y1 + ((y2 - y1) * ((row)/(len(board))))) , # spillgrid
                                        (x1 + ((x2 - x1) * ((col + 1)/(len(board[0]))))), ((y1 + ((y2 - y1) * ((row + 1)/(len(board)))))), 
                                        fill = colorboard[row][col], width = 0 )
                if board[row][col] == -2: #poeng
                    canvas.create_rectangle(((x1 + ((x2 - x1) * ((col)/(len(board[0]))))) + (app.width/60), (y1 + ((y2 - y1) * ((row)/(len(board))))) + (app.height/40), # spillgrid
                                           (x1 + ((x2 - x1) * ((col + 1)/(len(board[0]))))) - (app.width/60)), ((y1 + ((y2 - y1) * ((row + 1)/(len(board)))))) - (app.height/40), 
                                            fill = "white", width = 0 )
                if debug_mode == True: # Debug posisjon for hver square
                    canvas.create_text((((((x2 - x1) * ((col)/(len(board[0]))))) + (((x2 - x1) * ((col + 1)/(len(board[0]))))))/2) + x1 , (((((y2 - y1) * ((row)/(len(board))))) + (((y2 - y1) * ((row + 1)/(len(board))))))/2) + y1 , text=f"{row},{col}\n{board[row][col]}",
                       fill='white')

def move_pacman(app):
    app.new_pos = get_next_head_position(app.head_pos[0], app.head_pos[1], app.direction)#hvor pacman flytter seg til
    if (app.board[app.head_pos[0]][app.head_pos[1]] >= 2 and app.ghoststate == "chase") == True: #sjekker for gameover
        app.state = "gameover"
        return
    if (app.new_pos == (10, 21) and app.direction == "east") == False: #sjekker om den ikke er på vei ut i "tunellen"
        if (app.board[app.new_pos[0]][app.new_pos[1]] == -2) == True: #sjekker om pacman tar poeng
            app.points += 1 #øker score
            app.board[app.new_pos[0]][app.new_pos[1]] == 0 #gjør poeng om til gulv
        if (app.board[app.head_pos[0]][app.head_pos[1]] >= 2 and app.ghoststate == "flee") == True: #sjekker om pacman tar spøkelser
            if app.board[app.head_pos[0]][app.head_pos[1]] == 2: #hvis blinky, blinky død
                app.blinkyval = 0
                app.board[app.blinkyrow][app.blinkycol] = 0
            elif app.board[app.head_pos[0]][app.head_pos[1]] == 3: #pinky
                app.pinkyval = 0
                app.board[app.pinkyrow][app.pinkycol] = 0
            elif app.board[app.head_pos[0]][app.head_pos[1]] == 4: #inky
                app.inkyval = 0
                app.board[app.inkyrow][app.inkycol] = 0
            elif app.board[app.head_pos[0]][app.head_pos[1]] == 5: #clyde
                app.board[app.clyderow][app.clydecol] = 0
                app.clydeval = 0
            app.points += 100 # spøkelse verdt 100 poeng
            app.board[app.new_pos[0]][app.new_pos[1]] == 0 #gjør poeng om til gulv 
        if (app.board[app.new_pos[0]][app.new_pos[1]] == -3) == True: #sjekker om pacman tar frukt
            app.points += 10 # frukt verdt 10 poeng
            app.board[app.new_pos[0]][app.new_pos[1]] == 0 #gjør poeng om til gulv
            app.ghoststate = "flee" #flee modus, spøkelser kan spises
            app.fleesound.start(loops=-1) #flee musikk starter
    if is_legal_move(app, app.new_pos[0], app.new_pos[1], app.board) == True: #sjekker om man kan flytte dit
        subtract_one_from_all_positives(app.board)# fjerner 1 slik at pacman "beveger" seg
        app.head_pos = app.new_pos #oppdaterer hodet
        if (app.board[app.head_pos[0]][app.head_pos[1]] >= 2 and app.ghoststate == "chase") == True: #sjekker og game over i ny posisjon
            app.state = "gameover"
            return
        app.board[app.head_pos[0]][app.head_pos[1]] = -1 #flytter pacman   
    elif (app.new_pos == (10, 21) and app.direction == "east") == True: #flytter seg fra høyre side av tunell til venstre
        subtract_one_from_all_positives(app.board)# fjerner 1 slik at pacman "beveger" seg
        app.head_pos = (10, 0) #venstre tunell
        if (app.board[app.head_pos[0]][app.head_pos[1]] >= 2 and app.ghoststate == "chase") == True:
            app.state = "gameover" #sjekker game over i tunnell
            return
        app.board[app.head_pos[0]][app.head_pos[1]] = -1 #flytter pacman
    elif (app.new_pos == (10, -1) and app.direction == "west") == True: # flytter seg fra venstre side av tunnell til høyre
        subtract_one_from_all_positives(app.board)# fjerner 1 slik at pacman "beveger" seg
        app.head_pos = (10, 20) #høyre tunnell
        if (app.board[app.head_pos[0]][app.head_pos[1]] >= 2 and app.ghoststate == "chase") == True:
            app.state = "gameover"
            return
        app.board[app.head_pos[0]][app.head_pos[1]] = -1 #flytter pacman

def move_ghost_blinky(app): #move funksjon for blinky (rød)
    if (app.blinkyval == 2): #Hvis iike død, kjør
        if (5 <= app.timer < 7) == True: #tvungen path 2 første moves, går ut av center
            app.prev_val_blinky = 0 
            app.board[app.blinkyrow][app.blinkycol] = 0
            app.blinkyrow -= 1
            app.blinkycol = 10
            app.board[app.blinkyrow][app.blinkycol] = app.blinkyval
        else:
            new_pos_blinky =   move_ghost_in_random_directions(app, app.board, app.blinkyrow, app.blinkycol, app.blinkyval) #henter verdier fra random for ny posisjon
            app.board[app.blinkyrow][app.blinkycol] = app.prev_val_blinky #oppdaterer brettet med den forrige verdien for å holde poeng i spillet #Veldig Buggy
            app.prev_val_blinky = new_pos_blinky[2] #sjekker hva som var originalt på forrige trekk
            app.blinkyval = new_pos_blinky[3]
            app.blinkyrow = new_pos_blinky[0] #ny blinky rad
            app.blinkycol = new_pos_blinky[1] #ny blinky col
            app.board[app.blinkyrow][app.blinkycol] = app.blinkyval #flytter blinky

def move_ghost_pinky(app): #samme som blinky, bare annen path
    if (app.pinkyval == 3):
        if (20 <= app.timer < 23) == True: #flytter pinky ut av center, tetter igjen plassen den sto på
            if (app.timer == 20) == True:
                app.prev_val_pinky = 1
                app.board[app.pinkyrow][app.pinkycol] = 1
                app.pinkyrow = 10
                app.pinkycol = 10
                app.board[app.pinkyrow][app.pinkycol] = app.pinkyval
            else:
                app.prev_val_pinky = 0
                app.board[app.pinkyrow][app.pinkycol] = 0
                app.pinkyrow -= 1
                app.pinkycol = 10
                app.board[app.pinkyrow][app.pinkycol] = app.pinkyval
        else:
            new_pos_pinky =   move_ghost_in_random_directions(app, app.board, app.pinkyrow, app.pinkycol, app.pinkyval)
            app.board[app.pinkyrow][app.pinkycol] = app.prev_val_pinky#Veldig Buggy
            app.prev_val_pinky = new_pos_pinky[2]
            app.pinkyval = new_pos_pinky[3]
            app.pinkyrow = new_pos_pinky[0]
            app.pinkycol = new_pos_pinky[1]
            app.board[app.pinkyrow][app.pinkycol] = app.pinkyval

def move_ghost_inky(app): #samme som pinky, men tetter ikke path, går ut av center
    if (app.inkyval == 4):
        if (35 <= app.timer < 37) == True:
            if (app.timer == 35) == True:
                app.prev_val_inky = 0
                app.board[app.inkyrow][app.inkycol] = 0
                app.inkyrow = 10
                app.inkycol = 10
                app.board[app.inkyrow][app.inkycol] = app.inkyval
            else:
                app.prev_val_inky = 0
                app.board[app.inkyrow][app.inkycol] = 0
                app.inkyrow -= 1
                app.inkycol = 10
                app.board[app.inkyrow][app.inkycol] = app.inkyval
        else:
            new_pos_inky =   move_ghost_in_random_directions(app, app.board, app.inkyrow, app.inkycol, app.inkyval)
            app.board[app.inkyrow][app.inkycol] = app.prev_val_inky#Veldig Buggy
            app.prev_val_inky = new_pos_inky[2]
            app.inkyval = new_pos_inky[3]
            app.inkyrow = new_pos_inky[0]
            app.inkycol = new_pos_inky[1]
            app.board[app.inkyrow][app.inkycol] = app.inkyval

def move_ghost_clyde(app): #samme som de andre, men tetter center helt
    if (app.clydeval == 5):
        if (50 <= app.timer < 53) == True:
            if (50 <= app.timer < 52) == True:
                app.prev_val_clyde = 1
                app.board[app.clyderow][app.clydecol] = 1
                app.clyderow = 10
                app.clydecol -= 1
                app.board[app.clyderow][app.clydecol] = app.clydeval
            else:
                app.prev_val_clyde = 1
                app.board[app.clyderow][app.clydecol] = 1
                app.clyderow -= 1
                app.clydecol = 10
                app.board[app.clyderow][app.clydecol] = app.clydeval
        else:
            new_pos_clyde =   move_ghost_in_random_directions(app, app.board, app.clyderow, app.clydecol, app.clydeval)
            app.board[app.clyderow][app.clydecol] = app.prev_val_clyde#Veldig Buggy
            app.prev_val_clyde = new_pos_clyde[2]
            app.clyderow = new_pos_clyde[0]
            app.clydecol = new_pos_clyde[1]
            app.clydeval = new_pos_clyde[3]
            app.board[app.clyderow][app.clydecol] = app.clydeval


def move_ghost_in_random_directions(app ,grid, ghost_row, ghost_col, ghost_val): #random ghost movement generator
    new_direction_added = False #sjekker om den har funnet en ny gyldig retning
    prev_val = 0 #variabel for forrige verdi spøkelse var på
    while new_direction_added == False: #finner ny ghostplass, er false hvis ikke gyldig plass
        new_direction = random.random() #genererer tall mellom 0 og 1
        if 0 <= new_direction <= 0.25: #east
            if (ghost_row == 10 and ghost_col + 1 == 21) == True:
                if grid[10][0] > 1:
                    continue
                else:
                    return [10, 0, 0, ghost_val]# flytter seg igjennom tunell
            elif grid[ghost_row][ghost_col + 1] > 1:
                continue #går ikke igjennom hvis noen er på andre siden
            elif (grid[ghost_row][ghost_col + 1] != 1 or grid[ghost_row][ghost_col + 1] == -1 or grid[ghost_row][ghost_col + 1] == -2) == True: #sjekker om dit den går er bakke, frukt eller pacman
                prev_val = grid[ghost_row][ghost_col + 1] #lagrer originalverdi til dit den skal
                new_direction_added = True #bekrefter ny retning
                if (grid[ghost_row][ghost_col + 1] == -1 and app.ghoststate ==  "chase") == True: #sjekker for game over
                    app.state = "gameover"
                    return [ghost_row, ghost_col + 1, prev_val, ghost_val]
                return [ghost_row, ghost_col + 1, prev_val, ghost_val] #returnerer ny posisjon + originalverdi til den posisjonen
        elif 0.25 < new_direction <= 0.5: #west
            if grid[ghost_row][ghost_col - 1] > 1:
                continue
            elif (grid[ghost_row][ghost_col - 1] == 0 or grid[ghost_row][ghost_col - 1] == -1 or grid[ghost_row][ghost_col - 1] == -2) == True:
                prev_val = grid[ghost_row][ghost_col - 1]
                new_direction_added = True
                if (grid[ghost_row][ghost_col - 1] == -1 and app.ghoststate ==  "chase") == True:
                    app.state = "gameover"
                    return [ghost_row, ghost_col - 1, prev_val, ghost_val]
                return [ghost_row, ghost_col - 1, prev_val, ghost_val]
        elif 0.5 < new_direction <= 0.75: #south
            if grid[ghost_row + 1][ghost_col] > 1:
                continue
            elif (grid[ghost_row + 1][ghost_col] != 1 or grid[ghost_row + 1][ghost_col] == -1 or grid[ghost_row + 1][ghost_col] == -2) == True:
                prev_val = grid[ghost_row + 1][ghost_col]
                new_direction_added = True
                if (grid[ghost_row + 1][ghost_col] == -1 and app.ghoststate ==  "chase") == True:
                    app.state = "gameover"
                    return [ghost_row + 1, ghost_col, prev_val, ghost_val]
                return [ghost_row + 1, ghost_col, prev_val, ghost_val]
        elif 0.75 < new_direction <= 1: #north
            if grid[ghost_row - 1][ghost_col] > 1:
                continue
            elif (grid[ghost_row - 1][ghost_col] != 1 or grid[ghost_row - 1][ghost_col] == -1 or grid[ghost_row - 1][ghost_col] == -2) == True:
                prev_val = grid[ghost_row - 1][ghost_col]
                new_direction_added = True
                if (grid[ghost_row - 1][ghost_col] == -1 and app.ghoststate ==  "chase") == True:
                    app.state = "gameover"
                    return [ghost_row - 1, ghost_col, prev_val, ghost_val]
                return [ghost_row - 1, ghost_col, prev_val, ghost_val]
        else:
            continue


def get_next_head_position(head_row, head_col, direction): #sjekker neste hodeplassering for pacman
    if direction == "east":
        return (head_row, head_col + 1)
    if direction == "west":
        return (head_row, head_col - 1)
    if direction == "south":
        return (head_row + 1, head_col)
    if direction == "north":
        return (head_row - 1, head_col)

def subtract_one_from_all_positives(grid): # -1 fra alle positive verdier på brett
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == -1: #sjekker for flere pacman
                grid[row][col] += 1

def is_legal_move(app ,row, col, board): #sjekker om verdi er innenfor brett og verdi <= 0
    if ((0 <= row < 21) and (0 <= col < 21)): #sjekker om det nye trekket er innenfor brettet
        if ((board[row][col] == 0) == True): #sjekker om bakke
            return True
        elif ((board[row][col] <= -2) == True): #sjekker om poeng
            return True
        elif ((board[row][col] == 1) == True): #sjekker om vegg
            return False
        elif ((board[row][col] > 1 and app.ghoststate == "flee") == True): #pac-man kan ta spøkelser i spisemodus
            return True
        elif ((board[row][col] > 1)): #sørger for at pacman kan gå på spøkelser
            return True
        else:
            return False # ellers utenfor brett

def add_superfruit_at_random_location(grid, app): #random spøkelsesspisefrukt generator
    new_superfruit_added = False #sjekker om frukt kan bli addet
    while new_superfruit_added == False: #finner ny fruktplasss, er false hvis ikke gyldig plass
        new_superfruit = [random.choice(range(len(grid))), random.choice(range(len(grid[0])))]
        if grid[new_superfruit[0]][new_superfruit[1]] == -2: #Hvis random plass har verdi -2, kan frukt være der
            app.board[new_superfruit[0]][new_superfruit[1]] = -3
            app.fruitspawntimer = 0 #resetter frukttimer
            new_superfruit_added = True

def redraw_all(app, canvas):
    draw_board(canvas, 25, 25, app.width-25, app.height-25, app.board, app.debug_mode, app) #brett
    if app.debug_mode == True: # debug text top
        canvas.create_text(app.width / 2, 10, text =f'{app.head_pos=} {app.direction=} {app.points=} {app.timer=} {app.ghoststate=} {app.blinkyval=}', fill ="black" )
    if app.state == "gameover": #gameover screen
        canvas.create_text(app.width / 2, app.height / 2, text ="GAME OVER!", font = "Helvetica 26 bold underline", fill ="white" )
        canvas.create_text(app.width / 2, app.height / 1.7, text =f"Your score was {app.points}, and you lasted for {app.timer} moves", font = "Helvetica 14 bold", fill ="white" )
        canvas.create_text(app.width / 2, app.height / 1.5, text ="Press Enter to restart", font = "Helvetica 14 bold", fill ="white" )
    if app.state == "complete": #level ferdig screen
        canvas.create_text(app.width / 2, app.height / 2, text ="LEVEL COMPLETE!", font = "Helvetica 26 bold underline", fill ="white" )
        canvas.create_text(app.width / 2, app.height / 1.7, text =f"Your score is {app.points}, and you used {app.timer} moves", font = "Helvetica 14 bold", fill ="white" )
        canvas.create_text(app.width / 2, app.height / 1.5, text ="Press Enter to continue", font = "Helvetica 14 bold", fill ="white" )

run_app(width=600, height=400, title="Pac-Man")


"""
Notater:

Spøkelser kan være veldig "seige" å spise til tider
kræsjer hvis 3 spøkelser lager en sandwich
kræsjer ofte hvis et spøkelse ikke kommmer seg ut av spawn og blir "muret inne" kan fikses ved å bla, fjerne premove og blokkering, eller å endre

Forslag til variasjoner til spøkelser:
Man kan gi alle spøkelsene en "personlighet" ved å endre preferanser til retningene. Hvis spøkelsene foretrekker forskjellige retninger, vil de oppføre seg annerledes fra hverandre
"""