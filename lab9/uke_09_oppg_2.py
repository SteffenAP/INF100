def mase_for_is():
    print("Kan jeg få en is?") #spør om is
    svar = input() #sjekker respons fra bruker
    while svar.lower() != "ja": #hvis respons ikke er ja
        print("Vær så snill, si ja!") #maser videre
        svar = input() #nytt svar
    print("Tusen takk!") #printes når while loop brytes

mase_for_is()