#Oppgave 2
#Lager en variabel for å lagre det nye resultatet
#Sjekker først om "shift-verdien" er større enn teksten
#Ikke vits i å rotere mer enn en runde
#Deretter sjekker den alle bokstaver i s
#Starter i shiftverdien, og jobber seg mot venstre

def rotate_string(s, k):
    rotation = ""
    while k > len(s):
        k -= len(s)
    x = len(s) - k
    for rotate in range(len(s)):
        rotation += s[-x]
        x = x - 1
    return rotation

#Assert oppgave 2
print("Tester rotate_string... ", end="")
assert(" World!Hello" == rotate_string("Hello World!", 5))
assert("bar" == rotate_string("bar", 0))
assert("arb" == rotate_string("bar", 1))
assert("rba" == rotate_string("bar", 2))
assert("bar" == rotate_string("bar", 3))
assert("arb" == rotate_string("bar", 4))
print("OK")