#Oppgave 3
def median(a):
    median = 0 # tom variabel for å lagre median
    newa = sorted(a) #ny a for å sortere listen
    index = (len(a)//2) # finne midten av listen
    if len(a) % 2 == 0: #partall betyr det er 2 tall i senter
        median = (((newa[index-1]) + (newa[index])) / 2)
    else: # ellers er det bare ett tall i senter
        median = newa[index]
    return median

#Assert oppgave 3
print("Tester median... ", end="")
assert(3 == median([1, 2, 3, 6, 7]))
assert(3.5 == median([1, 2, 3, 4, 6, 9]))
a = [-10, 100, 8, 7, 2]
assert(7 == median(a))
assert([-10, 100, 8, 7, 2] == a) # Sjekker at funksjonen ikke er destruktiv
print("OK")