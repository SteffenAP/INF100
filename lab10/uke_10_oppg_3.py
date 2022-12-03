import copy

#Oppgave 3
def filter_words(words, must_include, must_exclude):
    finallist = copy.deepcopy(words) #kopierer ordlisten i en muterbar liste
    for word in words: # for hvert ord
        for incletter in must_include: #for hver bokstav i must include
            if incletter in word: #hvis bokstav i ord
                continue #sjekk neste
            else:
                finallist.remove(word) # hvis ikke i, fjern ord fra liste
        for excletter in must_exclude: #for hver bokstav i must exclude
            if word not in finallist: #ord kan allerede ha blitt slettet, hopp over hvis det er tilfellet
                break
            if excletter not in word: #hvis bokstav ikke i ord, fortsett
                continue
            else: #ellers fjern
                finallist.remove(word)
    return finallist #returner mutert liste


#Oppgave 3 assert
print("Tester filter_words... ", end="")
word_list = ["kattepus", "hundevofs", "kosebamse", "kanintuss", "slangesvin"]
must_include = {"a", "s"}
must_exclude = {"m", "v"}
expected_value = ["kattepus", "kanintuss"]
assert(expected_value == filter_words(word_list, must_include, must_exclude))

word_list = ["abc", "abd", "adc", "dbc", "abcx", "abyc", "azbc", "dcba"]
must_include = {"a", "b", "c"}
must_exclude = {"x", "y", "z"}
expected_value = ["abc", "dcba"]
assert(expected_value == filter_words(word_list, must_include, must_exclude))
print("OK")