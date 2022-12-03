import random
from uib_inf100_graphics import *
import copy

def restart(app): #starter spillet
    app.playstate = True #Sjekker for pause
    app.debug_mode = True #Starter i debug
    app.head_pos = (3, 3) #Hvor hodet starter
    app.snake_size = 3 #Startverdi til slange
    app.board = [] #Tomt brett(bestemmes av bruker)
    app.direction = "east" #Startretning slange"
    if app.state == "active": #Hvis kravene for å starte oppfylles
        for _ in range(app.board_size):
            app.board.append([0]*app.board_size) #Lager en grid basert på ønsker størrelse av bruker
        app.board[3][3] = 3 #hode start
        app.board[3][2] = 2#kropp start
        app.board[3][1] = 1 #kropp start
        add_apple_at_random_location(app.board) #Frukt til å starte med


def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.board_size = 5 #Brettet kan ikke være mindre enn 5x5
    app.state = "start" #Startmeny
    app.ent_board = False #Det har ikke blitt skrevet inn ønsket brettstørrelse enda
    restart(app)# Starter spillet



def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.debug_mode == False and app.state == "active" and app.playstate == True: #Slangen flytter seg hvis debug er av, 
                                                                                    #spillet er klar til å starte, og ikke på pause
        move_snake(app)

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if event.key == "b" and app.state == "start": #Går ut av startskjerm hvis man trykker b
        app.state = "input" #state hvor man bestemmer brettstørrelse
        restart(app) #kjører spill
    if event.key == "d": #debug toggle
        app.debug_mode = not app.debug_mode
    if event.key == "p": #pause toggle
        app.playstate = not app.playstate
    if app.state == "active" and app.playstate == True: #Hvis spill i gang og ikke på pause
        if event.key == "Up":# gå opp
            app.direction = "north"
        if event.key == "Down": # gå ned
            app.direction = "south"
        if event.key == "Right": # gå høyre
            app.direction = "east"
        if event.key == "Left": #gå venstre
            app.direction = "west"
    if app.debug_mode == True: # gå med space i debug
        if event.key == "Space":
            move_snake(app)
    if app.state == "gameover": # game over state
        if event.key == "Backspace": # restartknapp
            app.state = "start" # tilbake til homescreen
            restart(app) # starter spill på nytt
    if app.state == "input": # hvis i brettstrl bestemmelses state
        if event.key == "w": #w øker størrelse
            app.board_size += 1
        if event.key == "s" and app.board_size > 5: #s senker strl, min 5 i strl
            app.board_size -= 1
        if event.key == "Enter": # bekreft valg
            app.state = "active" # klar til å starte
            restart(app) #kjør spill
 
def draw_board(canvas, x1, y1, x2, y2, board, debug_mode):
        colorboard = copy.deepcopy(board) # kopierer brettet for å finne farger
        for row in range(len(board)):# For hver rad, gjør følgende for hver kolonne i raden
            for col in range(len(board[0])):
                if board[row][col] < 0: #Frukt
                    colorboard[row][col] = "#CF5B5C"
                if board[row][col] == 0: #Bakke
                    colorboard[row][col] = "#e3c08f"
                if board[row][col] > 0: #slange
                    colorboard[row][col] = "#53943D"
                canvas.create_rectangle((x1 + ((x2 - x1) * ((col)/(len(board[0]))))), (y1 + ((y2 - y1) * ((row)/(len(board))))) , # spillgrid
                                        (x1 + ((x2 - x1) * ((col + 1)/(len(board[0]))))), ((y1 + ((y2 - y1) * ((row + 1)/(len(board)))))), 
                                        fill = colorboard[row][col], width = 0 )
                if debug_mode == True: # Debug posisjon for hver square
                    canvas.create_text((((((x2 - x1) * ((col)/(len(board[0]))))) + (((x2 - x1) * ((col + 1)/(len(board[0]))))))/2) + x1 , (((((y2 - y1) * ((row)/(len(board))))) + (((y2 - y1) * ((row + 1)/(len(board))))))/2) + y1 , text=f"{row},{col}\n{board[row][col]}",
                       fill='black')

def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos[0], app.head_pos[1], app.direction)#hvor hode flytter seg til
    if is_legal_move(app.head_pos[0], app.head_pos[1], app.board) == False: #sjekker om man kan flytte dit
        app.state = "gameover"# game over
        return app.state #slutter å flytte
    if app.board[app.head_pos[0]][app.head_pos[1]] == -1: #sjekker om slangen tar frukt
        app.snake_size += 1 #øker slangestrl
        add_apple_at_random_location(app.board) # nytt eple
    else:
        subtract_one_from_all_positives(app.board)# fjerner 1 slik at slangen "beveger" seg
    app.board[app.head_pos[0]][app.head_pos[1]] = app.snake_size #flytter hode

def add_apple_at_random_location(grid): #random eple generator
    new_apple_added = False #sjekker om eple kan bli addet
    while new_apple_added == False: #finner ny epleplass, er false hvis ikke gyldig plass
        new_apple = [random.choice(range(len(grid))), random.choice(range(len(grid[0])))]
        if grid[new_apple[0]][new_apple[1]] == 0: #Hvis random plass har verdi 0, kan eple være der
            grid[new_apple[0]][new_apple[1]] = -1
            new_apple_added = True
        

def get_next_head_position(head_row, head_col, direction): #sjekker neste hodeplassering
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
            if grid[row][col] > 0:
                grid[row][col] -= 1

def is_legal_move(row, col, board): #sjekker om verdi er innenfor brett og verdi <= 0
    if ((0 <= row < len(board)) and (0 <= col < len(board[0]))):
        if ((board[row][col] <= 0) == True):
            return True
        else:
            return False
    else:
        return False


def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    canvas.create_rectangle(0, 0, app.width, app.height, fill= "#B9C68F" ) #bakgrunn
    draw_board(canvas, 25, 25, app.width-25, app.height-25, app.board, app.debug_mode) #brett
    if app.debug_mode == True: # debug text top
        canvas.create_text(app.width / 2, 10, text =f'{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}', fill ="black" )
    if app.state == "gameover": #gameover screen
        canvas.create_text(app.width / 2, app.height / 2, text ="GAME OVER!", font = "Helvetica 26 bold underline", fill ="black" )
        canvas.create_text(app.width / 2, app.height / 1.7, text ="Press Backspace to restart", font = "Helvetica 14 bold", fill ="black" )
    if app.state == "start": #startscreen
                canvas.create_text(app.width / 2, app.height / 2, text =
        """Welcome to Snake! \n
        The goal of the game is to grow as big as possible without \n
        colliding with yourself or the wall. \n
        You grow by eating apples \n
        When you press "b", this screen will dissapear, and you will \n
        have the option of increasing or decreasing your \n
        board size, minimum value is 5 \n
        After that, press "d" to start the game \n
        Legend: \n
        Arrow keys: Change the direction of your snake \n
        d: Debug mode, In debug mode, press space to move once \n
        p: Pause. This will also bring up the legend again \n
        If you lose: press Backspace to restart
        """  , 
        font = "Ariel 8 bold", fill ="blue" )
    if app.state == "input": #brett input screen
        canvas.create_text(app.width / 2, app.height / 2, text =f"The Board size is: {app.board_size :}\n\nPress w to increase\n\nPress s to decrease\n\nMinimum value is 5\n\nPress Enter to start\n",
                             font = "Ariel 16 bold", fill = "blue" )
    if app.playstate == False: #pausemeny
                canvas.create_text(app.width / 2, app.height / 2, text =
        """Pause! \n
        If you haven't started the game yet\n
        Press "p" and "d" after entering board size in terminal
        Press "p" to unpause \n
        Legend: \n
        Arrow keys: Change the direction of your snake \n
        d: Debug mode, In debug mode, press space to move once \n
        p: Pause \n
        If you lose: press Backspace to restart
        """  , 
        font = "Ariel 8 bold", fill ="blue" )

run_app(width=500, height=400, title="Snake")