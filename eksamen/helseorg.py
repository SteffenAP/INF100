import csv

#Det eneste man trenger å gjøre for å få dette programmet til å kjøre er bytte ut hva som står etter = i innmat med navnet på de gamle medisinlistene inni ""
#Så bytte ut hva som står etter = i utskrift med hva du vil kalle den nye medisinlisten inni "", husk å avslutte navnet med .csv
#Deretter er det bare å trykke på spill av/kjør knappen oppi høyre hjørne, så skal den nye listen dukke opp i kolonnen til venstre, under "EXPLORER"


innmat = "sample_input.csv"
utskrift = "expected_output.csv"

with open(innmat, "r", encoding='utf-8') as f:
    sample = list(csv.reader(f, delimiter=","))
innhold = sample[1:]

newformat = [['personnummer', 'medisin', 'startdato', 'endring']]

def sorter_data_til_nytt_format(data):
    for line in data:
        newformat.append([line[0],line[1],line[2],1])
        newformat.append([line[0],line[1],line[3],0])
    return newformat

def skriv_nytt_format_til_csvfil(data):
    content = sorter_data_til_nytt_format(data)
    with open(utskrift, "w", encoding='utf-8', newline = '') as f:
        skrivline = csv.writer(f)
        for row in content:
            skrivline.writerow(row)



skriv_nytt_format_til_csvfil(innhold)
