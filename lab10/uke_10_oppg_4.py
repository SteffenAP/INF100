#Oppgave 4
def people_with_age(path, age):
    rightpeople = set() #Output skal være set, 
    people = open(path, encoding = 'utf-8') #åpner filen, med utf-8 encoding for ø i Frøya
    listpeople = [line.strip() for line in people] #Deler filen inn i en liste, der hvert innlegg har en person og den alder
    for person in listpeople: #sjekker hver person
        if str(age) in person: #Hvis alderen er i person
            addedperson = (person.split(" "))[0] #Fjerner alder, slik at bare personen blir lagt til
            rightpeople.add(addedperson) #legger til person i set
    return rightpeople

#Assert oppgave 4
assert(people_with_age('namesages.txt', 18) == {'Odin', 'Trym'})
assert(people_with_age('namesages.txt', 19) == {'Brage', 'Embla', 'Idun',
                                                'Astrid', 'Gro'})
assert(people_with_age('namesages.txt', 20) == {'Alf', 'Frøya', 'Edda'})
assert(people_with_age('namesages.txt', 21) == {'Thor'})
assert(people_with_age('namesages.txt', 22) == {'Geir'})
assert(people_with_age('namesages.txt', 23) == set())