#Oppgave 1a
def at_least_two(word, c):
    if word.count(c) >= 2: #Teller forekomster av c
        return True #Hvis 2 eller fler, True
    else:
        return False

#Oppgave 1b
def at_least_two_in_list(wordlist, c):
    wordcount = 0 #Teller
    for word in wordlist: #For hvert ord i lisa
        if word.count(c) >= 2: #Hvis 2 eller flere, +1
            wordcount += 1
    return wordcount #return teller

#Oppgave 1c
def at_least_two_in_file(path, c):
    wordfile = open(path) #åpner fil
    wordlist =[line.strip() for line in wordfile] #Gjør fil om til liste
    return at_least_two_in_list(wordlist, c) #kjører forrige funksjon med ny liste


#Assert 1a
print("Tester at_least_two... ", end="")
assert(at_least_two('assessment', 's'))
assert(at_least_two('eksamen', 'e'))
assert(not at_least_two('gradering', 'd'))
assert(at_least_two('grunnleggende', 'e'))
assert(not at_least_two('midterm', 'x'))
print("OK")


#Asser 1b
print("Tester at_least_two_in_list... ", end="")
words = ['exam', 'christmas', 'assessment', 'test', 'paper', 'class']
assert(3 == at_least_two_in_list(words, 's'))
assert(1 == at_least_two_in_list(words, 'e'))
assert(0 == at_least_two_in_list(words, 'a'))
print("OK")

#Assert 1c
print("Tester at_least_two_in_file... ", end="")
assert(4==at_least_two_in_file('wordlist.txt', 's'))
assert(1==at_least_two_in_file('wordlist.txt', 'e'))
assert(0==at_least_two_in_file('wordlist.txt', 'a'))
print("OK")