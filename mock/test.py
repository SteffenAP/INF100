def prisregning():
    pris = 100
    øk = 1.5
    senk = 0.5
    pris = pris * øk
    pris = pris * senk
    pris = pris * øk
    pris = pris * senk
    pris = pris * øk
    pris = pris * senk
    return pris
print(prisregning())