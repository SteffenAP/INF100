#Oppgave 5
#Lagrer felles symboler i en variabel og returnerer variablen til slutt
#Hvis variablen allerede er i common lagres den ikke dobbelt
#Sjekker om hvert enkelt tegn i s1 har medlemskap i s2
def get_common_symbols(s1, s2):
    common = ""
    for character in s1:
        if character in common:
            continue
        if character in s2:
            common += character
    return common

#Assert oppgave 5
print("Tester get_common_symbols... ", end="")
assert("" == get_common_symbols("foo", "bar"))
assert("fo" == get_common_symbols("foo", "foo"))
assert("Hvr e,a" == get_common_symbols("Hvor er du, Kari?", 
                                       "Her er jeg, Olav!"))
print("OK")

