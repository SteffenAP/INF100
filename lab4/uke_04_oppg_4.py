#Oppgave 4a
#Sjekker om en kode har god stil
#Deler opp koden i linjer, og sjekker om linje er mindre eller lik 80
def good_style(source_code):
    for line in source_code.splitlines():
        if len(line) >= 80:
            return False
    else: 
        return True

#Oppgave 4b
#Sjekker om filer følger god kode stil
#leser av filinnhold til variabel, og kjører
#funksjonen fra 4a med variabelen
def good_style_from_file(filename):
    with open(filename, "rt") as f:
        contents = f.read()
        return good_style(contents)

#Assert 4a

print("Tester good_style... ", end="")
assert(good_style("""\
def distance(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
"""))
assert(good_style((("x" * 79) + "\n") * 20))
assert(not good_style((("x" * 79) + "\n") * 5 +
                      (("x" * 80) + "\n")     +
                      (("x" * 79) + "\n") * 5))
print("OK")


#Assert 4b

print("Tester good_style_from_file... ", end="")
assert(good_style_from_file("test_file1.py"))
assert(not good_style_from_file("test_file2.py"))
assert(not good_style_from_file("test_file3.py"))
assert(good_style_from_file("uke_04_oppg_4.py"))
print("OK")