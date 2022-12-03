import csv
import matplotlib.pyplot as plt

# Lese inn filen
with open("Akvakulturregisteret.csv", "rt", encoding='iso-8859-1') as f:
    tabell = list(csv.reader(f, delimiter=";"))

# Dele opp tabellen i kolonnenavn (overskifter) og data
headers = tabell[1]
data = tabell[2:]

# Konverter alle tallverdier fra streng til float
for row in data:
    for i in range(len(row)):
        try:
            row[i] = float(row[i])
        except ValueError:
            pass

# Lage oppslagsverk kolonnenavn -> kolonnenummer (i)
colname_to_i = {}
for i in range(len(headers)):
    colname_i = headers[i]
    colname_to_i[colname_i] = i

# Filtrer data slik at vi kun har rader hvor gitt kolonne matcher verdi
def filter_data(data, col_num, must_match_value):
    filtered_data = []
    for row in data:
        cell_value = row[col_num]
        if cell_value in must_match_value:
            filtered_data.append(row)
    return filtered_data

# Filtrerer data: finner punkter hvor vannmiljø er ferskvann og saltvann
laks_data = filter_data(data, colname_to_i["ART"], "Laks")
orret_data = filter_data(data, colname_to_i["ART"], "Ørret")
annet_data = filter_data(data, colname_to_i["ART"], "")

# Hent ut en gitt kolonne
def get_col(data, col_num):
    col = []
    for row in data:
        col.append(row[col_num])
    return col

# Plot saltvannsanlegg 
orret_xs = get_col(orret_data, colname_to_i["Ø_GEOWGS84"])
orret_ys = get_col(orret_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=orret_xs, y=orret_ys, alpha=0.2, s=20, label="Ørret")

# Plot ferskvannsanlegg 
laks_xs = get_col(laks_data, colname_to_i["Ø_GEOWGS84"])
laks_ys = get_col(laks_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=laks_xs, y=laks_ys, alpha=0.2, s=20, label="Laks")

# Plot ferskvannsanlegg 
annet_xs = get_col(annet_data, colname_to_i["Ø_GEOWGS84"])
annet_ys = get_col(annet_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=annet_xs, y=annet_ys, alpha=0.2, s=20, label="Annet")


plt.legend()
plt.show()