#Oppgave 4
def find_words_in_character_grid(char_grid, words):
    comp = ""
    complist = []
    for word in words: #for hvert ord
            for row in range(len(char_grid)):# Sjekker hver rad
                for col in range(len(char_grid[0])): #Hver indeks i hver rad
                    comp += char_grid[row][col] #lager raden om til en string
                if word in comp: #sjekker om ordet er i string
                    if word not in complist: #eliminerer duplikater
                        complist.append(word) # legger til ord i liste
                    comp = "" # tømmer string for neste rad

            for col2 in range(len(char_grid[0])): # samme som forrige, bare for kolonner
                for row2 in range(len(char_grid)):
                    comp += char_grid[row2][col2]
                if word in comp:
                    if word not in complist:
                        complist.append(word)
                    comp = ""
    return complist


#Assert 
print("Tester find_words_in_character_grid... ", end="")

glossary = ["dikt", "hus", "lese", "by", "elev",
            "smart", "helt", "mål", "yr", "lære"]
char_grid= [
        ['d','s','h','s','s','y'],
        ['l','æ','r','e','s','å'],
        ['k','a','l','a','m','e'],
        ['t','h','e','r','a','q'],
        ['e','t','s','t','r','z'],
        ['e','t','e','r','t','p'],
        ['e','m','å','l','v','w'],
    ]
found_words = find_words_in_character_grid(char_grid, glossary)
assert(sorted(['lese', 'smart', 'mål', 'lære']) == sorted(found_words))
print("OK")
