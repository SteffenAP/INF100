def tid_til_nok_egenkapital():
    aarslonn = int(input("Hva er årslønn? "))
    sparing = int(input("Hvor mange prosent spares? "))
    bolig = int(input("Hvor mye koster boligen? "))
    maaned = 0
    egenkapital = 0 
    while egenkapital <= bolig * 0.25:
        rente = (egenkapital * 0.04)/12
        egenkapital += rente
        egenkapital += (aarslonn * (sparing/100))/12
        rente = (egenkapital * 0.04)/12
        maaned += 1
    print(f"Det tar {maaned} måneder å spare nok egenkapital")

tid_til_nok_egenkapital()
