#Oppgave 7
def students_who_passed(path):
    exams = [] #de som kan ta eksamen
    f = open(path)
    flist = [line.strip() for line in f] #gjør csv om til liste med hver student og score i index
    for i in range(len(flist)): # sjekker alle studenter
        if i == 0: #ignorerer tags
            continue
        convert =  flist[i] #gjør om til string for å lettere fjerne ;
        nlist = convert.split(";")#fjerner ;
        if nlist[13] == nlist[14] == nlist[15] == nlist[16] == "B": #sjekker quiz
            if nlist.count("B") >= 10 or nlist[1] == "B": #sjekker om 6 laber har stått eller kartleggingsprøve
                if nlist[8:13].count("B") >= 3: #sjekker de 5 siste labene
                    exams.append(nlist[0]) # legger til eleven hvis alle krav oppfylles
    return exams


#Assert
print("Tester students_who_passed... ", end="")
assert(['abc101', 'abc103', 'abc105', 'abc109', 'abc111', 'abc113'] 
        == students_who_passed("course_data.csv"))
print("OK")
