
#Oppgave 1
#Man setter inn en verdi et sted i source teksten
#teksten deles på punktet man vil ha verdien, 
#og verdien legges til i det punktet
def insert_at(source_string, index, insertion_string):
    return str(source_string[:index] + insertion_string + source_string[index:])

#Assert oppgave 1
print("Tester insert_at... ", end="")
assert("XYabcd" == insert_at("abcd", 0, "XY"))
assert("abXYcd"== insert_at("abcd", 2, "XY"))
assert("abcdXY"== insert_at("abcd", 4, "XY"))
print("OK")