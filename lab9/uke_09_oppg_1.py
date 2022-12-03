#Oppgave 1

def will_work(city, salary):
    if city.lower() == "bergen": #hvis input city i lowercase er bergen
        if salary >= 400000: #Hvis lønn er lik eller over 400 000
            return True #Ja
        else: #Ellers
            return False #Nei
    elif city.lower() == "bodø": #Hvis input city i lowecase er bodø
        if salary >= 900000: #Hvis lønn er lik eller over 900 000
            return True #Ja
        else: #Ellers Nei
            return False # Nei
    elif city.lower() == "verdensrommet": #Hvis input city i lowercase er verdensrommet
        return True # Ja
    elif salary >= 600000: #Hvis ingen av de andre kravene treffes, men lønn er over eller lik 600 000
        return True #Ja
    else: #Ellers
        return False# Nei

#Assert oppgave 1
print("Tester will_work...", end="")
assert(will_work('Bergen', 400_000))
assert(not will_work('Bergen', 399_999))
assert(not will_work('Kristiansand', 590_000))
assert(will_work('Bodø', 900_000))
assert(will_work('Tromsø', 600_000))
assert(not will_work('Bodø', 899_999))
assert(will_work('Verdensrommet', 10))
print("OK")
    