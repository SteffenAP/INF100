#Oppgave 6, del a

def compress(raw_binary):
    result = "" # resultat av komprimering
    counter = 1 #teller antall i succession
    if raw_binary[0] != "0":
        result += "0 " # legger til 0 først hvis første ikke er 0
    for i in range(len(raw_binary)):
        if (i + 1) == len(raw_binary):
            result += str(counter) # når den er på siste tall, legger den til den nåværende total
            break #avslutter
        if raw_binary[i] == raw_binary[i+1]:
            counter += 1 #hvis to tall er like, økes counter
        else:
            result += str(counter) + " " # når to tall er ulike, legges counten til
            counter = 1 #reset count
    return result

#del b
def decompress(compressed_binary):
    result = ""
    listcompbi = compressed_binary.split(" ") #gjør tallene i input til liste
    if listcompbi[0] != 0: #sjekker om første tall er 0 for å se hvilket tall man starter med
        for i in range(len(listcompbi)):
            if i % 2 == 0: #legger til 0 * verdi på partalls index
                result += ("0" * int(listcompbi[i]))
            else: # 1 på oddetallsindex
                result += ("1" * int(listcompbi[i]))
    else: # motsatt av forrige
        for i in range(len(listcompbi)):
            if i % 2 == 0:
                result += ("1" * int(listcompbi[i]))
            else:
                result += ("0" * int(listcompbi[i]))
    return result

#Assert del a
print("Tester compress... ", end="")
assert("2 3 4 4" == compress("0011100001111"))
assert("0 2 1 8 1" == compress("110111111110"))
assert("4" == compress("0000"))
print("OK")

#Assert del b
print("Tester decompress... ", end="")
assert("0011100001111" == decompress("2 3 4 4"))
assert("110111111110" == decompress("0 2 1 8 1"))
assert("0000" == decompress("4"))
print("OK")