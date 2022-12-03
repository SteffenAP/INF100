def oppdrettsanleggliste(path):
    art = {} #tom dict
    artlist = [] #tom liste
    f = open(path, "r") #variabel for path
    register = f.read() #path content
    for line in register.splitlines(): #for linje i register
        if (line.split(";")[12] in art) == True: #Hvis art i liste
            art[line.split(";")[12]] += 1 #øk art
        else:
            art[line.split(";")[12]] = 1 #legg til art
    sortedartdict = sorted(art.items()) #sortert dict
    for key, value in sortedartdict: #gjør dict om til liste
        artlist.append(f"{key}: {value}")
    artlist.pop(0) #fjerner " " og "ART"
    artlist.pop(0)
    for line in artlist:
        print(line)

print(oppdrettsanleggliste("Akvakulturregisteret.csv"))