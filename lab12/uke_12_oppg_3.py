def spise_sammen():
    meny = ["Stekt uer med blomkålpuré", "Piggvarfilet med ertepuré", "Boknatorsk med kremstuede",  "Steinbit, sjøkreps og snøkrabbe", "Norske oster med marmelade"] #menyliste
    print("""
Meny

1. Stekt uer med blomkålpuré.
2. Piggvarfilet med ertepuré.
3. Boknatorsk med kremstuede.
4. Steinbit, sjøkreps og snøkrabbe.
5. Norske oster med marmelade.
""")
    order = input("Hvilket nummer vil du bestille? ") #variabel for brukerinput
    try: #prøver input
        placedorder = meny[int(order) - 1] #input -1 for riktig listeindex
    except:
        print("Beklager, det er ikke et gyldig valg!") #hvis kræsj, print dette
    else:
        print(f"{placedorder} kommer straks!") #ellers print dette

spise_sammen()