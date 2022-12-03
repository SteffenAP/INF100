import csv

with open("NO_ADM12.csv", "rt", encoding='utf-8') as f:
    tabell = list(csv.reader(f, delimiter=";"))
header = tabell[:1]
content = tabell[1:]

def filter_fylke(content, filter): 
    filtered_content = ""
    for row in content:
        cell = row[1]
        if filter in cell and row[5] == "ADM1":
            filtered_content = row[7]
    return filtered_content

def filter_adm(content, filter):
    filtered_content = dict()
    for row in content:
        cell = row[5]
        if filter == cell:
            filtered_content[row[1]] = row[7]
    return filtered_content

def filter_kommune_by_size(content, filter):
    filtered_content = list()
    for row in content:
        cell = row[7]
        if filter == cell:
            filtered_content.append([int(row[9]), row[1]])
    return filtered_content

def filter_kommune(content, filter):
    filtered_content = list()
    for row in content:
        cell = row[7]
        if filter == cell:
            filtered_content.append(row[1])
    return filtered_content

def filter_kommune_by_pos(content, filter):
    filtered_content = list()
    for row in content:
        cell = row[7]
        if filter == cell:
            filtered_content.append([float(row[3]), row[4], row[1]])
    return filtered_content

def print_county(county):
    fylkenr = filter_fylke(content, str(county))
    kommuner = filter_kommune_by_size(content, fylkenr)
    sizekom = sorted(kommuner)
    pos = filter_kommune_by_pos(content, fylkenr)
    sortpos = sorted(pos)
    print(
f"""
=====================================
{sizekom[-1][1]}
=====================================
{sizekom[-2][1]}:   {sizekom[-2][0]}
{sizekom[0][1]}:    {sizekom[0][0]}
{sortpos[-1][2]}:   {sortpos[-1][0]} N  {sortpos[-1][1]} Ø
{sortpos[0][2]}:    {sortpos[0][0]} N  {sortpos[0][1]} Ø
=====================================
""")

def registry():
    userinput = ""
    while userinput != "q":
        userinput = input("Which county (q to quit)? ")
        if userinput == "q":
            break
        try:
            print_county(userinput)
        except:
            print("No matching county found. Try again.")
    print("Bye!")

registry()

