#Oppgave 5, del a

def can_be_made_of_letters(word, letters):
    for i in range(len(word)): # sjekker om det finnes like mange av en bokstav i ord og bokstavlisten
        if word.count(word[i]) <= letters.count(word[i]):
            continue
        else:
            return False
    return True

#Del b
def possible_words(wordlist, letters):
    allwords = [] #gjentar del a for hvert ord i wordlist
    for i in range(len(wordlist)):
        if can_be_made_of_letters(wordlist[i], letters) == True:
            allwords.append(wordlist[i])
    return allwords

def possible_words_from_file(path, letters):
    f = open(path) # gjør om alle linjer i path til en verdi i en liste
    flist = [line.strip() for line in f] 
    return possible_words(flist, letters)# kjører listen og bokstavene igjennon b

#assert del a
print("Tester can_be_made_of_letters... ", end="")
assert(can_be_made_of_letters("emoji", "abcdefghijklmno"))
assert(not can_be_made_of_letters("smilefjes", "abcdefghijklmnopqrs"))
assert(can_be_made_of_letters("smilefjes", "abcdeeefghijklmnopqrsss"))
assert(can_be_made_of_letters("lese", "esel"))
print("OK")

#assert del b
print("Tester possible_words... ", end="")
hundsk =["tur", "mat", "kos", "hent", "sitt", "dekk", "voff"]
kattsk =["kos", "mat", "pus", "mus", "purr", "mjau", "hiss"]

assert(['kos', 'sitt'] == possible_words(hundsk, "fikmopsttuv"))
assert(['kos', 'pus', 'mus'] == possible_words(kattsk, "fikmopsttuv"))
print("OK")

#assert del c
print("Tester possible_words_from_file... ", end="")
assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
        == possible_words_from_file("nsf2022.txt", "hund"))
print("OK")