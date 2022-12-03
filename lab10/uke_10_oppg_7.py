import random
import math

def distance(x1, y1, x2, y2): #henter avstandsfunksjon fra uke1, oppg5b
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


def find_pi(n):
    counter = 0 #teller antall ganger i sentrum
    for _ in range(n): #gjennomfører løkken like mange ganger som skrevet inn
        randomnumberx = ((random.random())*2)-1 #random x koordinat
        randomnumbery = ((random.random())*2)-1 #random y koordinat
        if distance(randomnumberx, randomnumbery, 0, 0) <= 1: #sjekker om punkt innenfor radius
            counter += 1 
    pi = (counter / n) * 4 #formel for pi 
    return pi 
