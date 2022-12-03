#Oppgave 3
#Del A

def sub_course_positions(path):
    position = {'forward': 0, 'depth': 0} #dict
    f = open(path, "r") #Åpner fil
    addedfile = f.read() #leser av filcontent
    for lines in addedfile.splitlines(): #deler variabel opp etter hver linje:
        if "forward" in lines: #Hvis linje er forward
            position["forward"] += int(lines.split(" ")[1]) #legg til verdi i forward til forward value
        elif "down" in lines: # hvis linje er down
            position["depth"] += int(lines.split(" ")[1]) #legg til verdi i depth
        elif "up" in lines: #hvis linje er up
            position["depth"] -= int(lines.split(" ")[1]) #fjern verdi i depth
        else:
            continue
    return position


#Del B
def sub_course(path):
    posdict = sub_course_positions(path) #henter resultat fra sub_course_pos
    sub_course_val = (posdict['forward'] * posdict['depth'])#Ganger verdier med hverandre
    return sub_course_val

#Assert Del A
print("Tester sub_course_positions... ", end="")
result = sub_course_positions("sub-path-sample.txt")
assert({'forward': 15, 'depth': 10} == result)
print("OK")

#Assert Del B
print("Tester sub_course_positions... ", end="")
result = sub_course_positions("sub-path-sample.txt")
assert({'forward': 15, 'depth': 10} == result)
print("OK")