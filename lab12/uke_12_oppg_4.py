import csv

def sum_of_column(path, col):
    with open(path, "r", encoding ='utf-8') as f:
        content = csv.reader(f) #leser av filens innhold til en var
        sum = float() #tom float variabel
        for row in content: #for linje i content
            try: #prøv å legge til flytvariabel
                sum += float(row[col])
            except: #ellers fortsett
                continue
    return sum

#Assert
print("Tester sum_first_col... ", end="")
assert(42.0 == sum_of_column("foo.csv", 0))
assert(95.0 == sum_of_column("foo.csv", 1))
assert(0.0 == sum_of_column("foo.csv", 2))
assert(76363.0 == sum_of_column("Statistikk_Tilsyn_ar.csv", 1))
assert(46007.0 == sum_of_column("Statistikk_Tilsyn_ar.csv", 2))
assert(5024518.0 == sum_of_column("airport-codes.csv", 3))
print("OK")