#oppgave 3
#Finner nte hendelse av et tegn
#Bruker en counter for å informere om når man har nådd n
#i antall hendelser
#bruker i for å spore nåværende indeks
#hvis counter ikke blir n, finnes ikke den nte hendelsen
def find_nth_occurence(search_string, character, n):
    counter = 0
    i = 0
    for letter in search_string:
        if letter == character:
            counter += 1
        if counter == n:
            return i
        i += 1
    if counter != n:
        return -1

#Assert oppgave 3
print("Tester find_nth_occurence... ", end="")
assert(0 == find_nth_occurence("abcabc", "a", 1))
assert(2 == find_nth_occurence("abcabc", "c", 1))
assert(-1 == find_nth_occurence("abcabc", "x", 1))
assert(3 == find_nth_occurence("abcabc", "a", 2))
assert(5 == find_nth_occurence("abcabc", "c", 2))
assert(-1 == find_nth_occurence("abcab", "c", 2))
print("OK")