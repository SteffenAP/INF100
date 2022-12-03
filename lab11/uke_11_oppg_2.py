#Oppgave 2
def add_markers(filename):
    displayedcontent = "" #tom string
    f = open(filename, "r", encoding='utf-8') #Åpner fil i utf-8
    addedfile = f.read() #leser av filcontent
    for lines in addedfile.splitlines(): #deler variabel opp etter hver linje
        displayedcontent += f">>>{lines}<<<\n" #legger til tegn
    return displayedcontent

#Assert
print("Tester add_markers... ", end="")
assert("""\
>>>Det var en gang en konge, og den kongen hadde hørt snakk om et skip som \
gikk like fort til lands som til vanns.<<<
>>>Så ville han også ha slikt et, og til den som kunne bygge det, lovte han \
ut kongsdattera og halve kongeriket, og det lyste han ut på kirkebakken ved \
alle kirkesogn over hele landet.<<<
>>>Det var mange som prøvde, kan du skjønne, for halve riket kunne være godt \
å ha, mente de vel, og kongsdattera kunne være bra å få i tillegg. Men ille \
gikk det med de fleste.<<<
""" == add_markers("askeladden.txt"))
print("OK")