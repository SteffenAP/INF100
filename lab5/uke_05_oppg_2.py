from uib_inf100_graphics import *

#Shrek

def redraw_all(app, canvas):

    #bein venstre
    canvas.create_polygon((150/400) * app.width, (130/200) * app.height, (190/400) * app.width, (130/200) * app.height, (175/400) * app.width, (180/200) * app.height, (135/400) * app.width, (180/200) * app.height, fill='saddle brown', outline='black')
    #bein høyre
    canvas.create_polygon((250/400) * app.width, (130/200) * app.height, (210/400) * app.width, (130/200) * app.height, (225/400) * app.width, (180/200) * app.height, (265/400) * app.width, (180/200) * app.height, fill='saddle brown', outline='black')
    #sko venstre
    canvas.create_polygon((175/400) * app.width, (180/200) * app.height, (100/400) * app.width, (180/200) * app.height, (110/400) * app.width, (195/200) * app.height, (175/400) * app.width, (195/200) * app.height, fill='black', outline='black')
    #sko høyre
    canvas.create_polygon((225/400) * app.width, (180/200) * app.height, (300/400) * app.width, (180/200) * app.height, (290/400) * app.width, (195/200) * app.height, (225/400) * app.width, (195/200) * app.height, fill='black', outline='black')
    #underskjorte
    canvas.create_oval((100/400) * app.width, (50/200) * app.height, (300/400) * app.width, (150/200) * app.height, fill='beige', outline='black')
    #skjorte tråd
    canvas.create_line((175/400) * app.width, (80/200) * app.height, (225/400) * app.width, (80/200) * app.height, fill='saddle brown', width=5)
    #skjorte venstre
    canvas.create_polygon((175/400) * app.width, (50/200) * app.height, (185/400) * app.width, (125/200) * app.height, (115/400) * app.width, (125/200) * app.height, (95/400) * app.width, (80/200) * app.height,
                      fill='saddle brown', width = 5, outline='black')
    #skjorte høyre
    canvas.create_polygon((225/400) * app.width, (50/200) * app.height, (215/400) * app.width, (125/200) * app.height, (285/400) * app.width, (125/200) * app.height, (305/400) * app.width, (80/200) * app.height, 
                      fill='saddle brown', width = 5, outline='black')
    #arm venstre
    canvas.create_polygon((95/400) * app.width, (80/200) * app.height, (120/400) * app.width, (105/200) * app.height, (70/400) * app.width, (165/200) * app.height, (50/400) * app.width, (160/200) * app.height,
                      fill='beige', width = 5, outline='black')
    #arm høyre                  
    canvas.create_polygon((305/400) * app.width, (80/200) * app.height, (280/400) * app.width, (105/200) * app.height, (330/400) * app.width, (165/200) * app.height, (350/400) * app.width, (160/200) * app.height,
                      fill='beige', width = 5, outline='black')
    #hånd venstre
    canvas.create_oval(((55 - 20)/400) * app.width, ((175 - 20)/200) * app.height, ((55 + 20)/400) * app.width, ((175 + 20)/200) * app.height, fill="olive drab", outline='black')
    #hånd høyre
    canvas.create_oval(((345 - 20)/400) * app.width, ((175 - 20)/200) * app.height, ((345 + 20)/400) * app.width, ((175 + 20)/200) * app.height, fill="olive drab", outline='black')
    #hode
    canvas.create_oval((150/400) * app.width, (10/200) * app.height, (250/400) * app.width, (60/200) * app.height,
                      fill='olive drab', width = 5, outline='black')
    #venstre øye 
    canvas.create_oval(((180 - 7)/400) * app.width, ((30 - 8)/200) * app.height, ((180 + 7)/400) * app.width, ((30 + 8)/200) * app.height, fill="white", outline='black')
    canvas.create_oval(((180 - 2)/400) * app.width, ((30 - 2)/200) * app.height, ((180 + 2)/400) * app.width, ((30 + 2)/200) * app.height, fill="tan4", outline='black')
    #høyre øye 
    canvas.create_oval(((220 - 7)/400) * app.width, ((30 - 8)/200) * app.height, ((220 + 7)/400) * app.width, ((30 + 8)/200) * app.height, fill="white", outline='black')
    canvas.create_oval(((220 - 2)/400) * app.width, ((30 - 2)/200) * app.height, ((220 + 2)/400) * app.width, ((30 + 2)/200) * app.height, fill="tan4", outline='black')

    #munn
    canvas.create_polygon((175/400) * app.width, (45/200) * app.height, (200/400) * app.width, (55/200) * app.height, (225/400) * app.width, (45/200) * app.height, (200/400) * app.width, (48/200) * app.height,
                      fill='black', width = 1, outline='black')
    #ører
    canvas.create_line((145/400) * app.width, (15/200) * app.height, (160/400) * app.width, (20/200) * app.height, fill='olive drab', width=8) #venstre "ørestilk"
    canvas.create_line((255/400) * app.width, (15/200) * app.height, (240/400) * app.width, (20/200) * app.height, fill='olive drab', width=8) #høyre "ørestilk"
    #venstre øre
    canvas.create_oval(((145 - 5)/400) * app.width, ((15 - 5)/200) * app.height, ((145 + 5)/400) * app.width, ((15 + 5)/200) * app.height, fill="green", outline='black')
    #høyre øre
    canvas.create_oval(((255 - 5)/400) * app.width, ((15 - 5)/200) * app.height, ((255 + 5)/400) * app.width, ((15 + 5)/200) * app.height, fill="green", outline='black')

run_app(width=400, height=200)