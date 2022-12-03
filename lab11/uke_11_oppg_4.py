#Oppgave 4
#Del A
def simplified_pig_latin(word):
    word = word.lower() #konverterer til lowercase
    pig_latin_word = "" #tom var
    vowel = {"a", "e", "i", "o", "u"} #vokalmengde
    if word[0] in vowel: #Hvis første bokstav er vokal
        pig_latin_word = f"{word}hay"
    else: #Hvis ikke
        pig_latin_word = f"{word[1:]}{word[0]}ay"
    return pig_latin_word

#Del B

def sentence_to_simplified_pig_latin(sentence):
    pig_latin_sentence = "" #tom variabel
    sentencelist = sentence.split(" ") #deler opp setning til liste
    for word in sentencelist: #løkke som kjører alle ord i setning igjennom forrige funksjon
        if word == sentencelist[-1]: #hvis siste, ikke space på slutten
            pig_latin_sentence += f"{simplified_pig_latin(word)}"
        else: #alle andre ord
            pig_latin_sentence += f"{simplified_pig_latin(word)} "
    return pig_latin_sentence

#Assert Del A
print("Tester simplified_pig_latin... ", end="")
assert("ellohay" == simplified_pig_latin("Hello"))
assert("imagehay" == simplified_pig_latin("Image"))
print("OK")

#Assert Del B
sentence = "My name is Sylvia Lavrans"
expected_value ="ymay amenay ishay ylviasay avranslay"
print("Tester sentence_to_simplified_pig_latin... ", end="")
assert(expected_value == sentence_to_simplified_pig_latin(sentence))
print("OK")