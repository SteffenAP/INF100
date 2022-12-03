def first_letter_last_word(path):
    storedletters = "" #Tom variabel
    f = open(path, "r", encoding='utf-8') #åpner path som f
    content = f.read() #innhold lagres i content
    for sentence in content.splitlines(): #for setning i splitlines
        storedletters += sentence.split(" ")[-1][0] #siste ord, første bokstav i sentence
    return storedletters

#Assert
print("Tester first_letter_last_word... ", end="")
assert("vlf" == first_letter_last_word("askeladden.txt"))
# Forklaring:
# Siste ord i første linje er 'vanns.'   Første bokstav i dette ordet er 'v'
# Siste ord i andre linje er 'landet.'   Første bokstav i dette ordet er 'l'
# Siste ord i tredje linje er 'fleste.'  Første bokstav i dette ordet er 'f'
print("OK")