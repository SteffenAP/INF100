#Leverer for moro skyld

#Oppgave 6
#Sjekker hvilken som er lengst av s1 og s2 for å hindre problemer
#med forskjellige lengder
#Deretter mikses strengene med s1 som prioritet
def mix(s1, s2):
    total = ""
    i = 0
    if len(s1) >= len(s2):
        for character in s1:
            if len(s1) != 0:
                total += character
            if len(s2) != 0 and len(s2)> i:
                total += s2[i]
            i += 1
    if len(s2) > len(s1):
        for character in s2:
            if len(s1) != 0 and len(s1)> i:
                total += s1[i]
            if len(s2) != 0:
                total += character
            i += 1
    return total

#Assert oppgave 6
print("Tester mix... ", end="")
assert("a1b2c3" == mix("abc", "123"))
assert("1a2b3c"== mix("123", "abc"))
assert("abc"== mix("abc", ""))
assert("abc"== mix("", "abc"))
assert("aAbBcde" ==mix("abcde", "AB"))
assert("aAbBCDE"== mix("ab", "ABCDE"))
print("OK")