#Leverer for moro skyld

from uke_04_oppg_3 import find_nth_occurence

#Del A, finne impact av et jordskjelv i en string i csv format
#Henter find_nth_occurence for å isolere impact i strengen, 
# og splicer med de indeksene

def get_impact(line):
    index_one = find_nth_occurence(line, ";", 2) + 1
    index_two = find_nth_occurence(line, ";", 3)
    impact = float(line[index_one:index_two])
    return impact

#Del B, filtrere ut jordskjelv under en viss impact
#Isolerer ut startstrengene som ikke har en impact
#Deretter sammenligne impact mot threshold med get_impact

def filter_earthquakes(earthquake_csv_string, threshold):
    result = ""
    for earthquake in earthquake_csv_string.splitlines():
        if earthquake.startswith('"""'):
            result += earthquake + "\n"
            continue
        if earthquake.startswith("id;"):
            result += earthquake + "\n"
            continue
        if get_impact(earthquake) >= float(threshold):
            result += earthquake + "\n"
    return result

#Del C

#Henter read og write file funksjoner fra inf100 siden

def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def write_file(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

#Lager en funksjon som leser av filen til en variabel, 
#og setter variabelen inn i funksjonen fra del B.
#Resultatet fra den forrige funksjonen lagres i target_filename

def filter_earthquakes_file(source_filename, target_filename, threshold):
    content_read = read_file(source_filename)
    new_content = filter_earthquakes(content_read, threshold)
    new_data = write_file(target_filename, new_content)
    return new_data


#Assert Del A
print("Tester get_impact... ", end="")
assert(1.43 == get_impact("nc72666881;California;1.43;2016-07-27 00:19:43"))
assert(4.9 == get_impact("us20006i0y;Burma;4.9;2016-07-27 00:20:28"))
print("OK")
#Assert Del B
print("Tester filter_earthquakes... ", end="")
assert("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
""" == filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 1.1))
assert("""\
id;location;impact;time
us20006i0y;Burma;4.9;2016-07-27 00:20:28
""" == filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 3.0))
assert("""\
id;location;impact;time
""" == filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 5.0))
print("OK")
#Assert Del C
print("Tester filter_earthquakes_file... ", end="")
filter_earthquakes_file("earthquakes_simple.csv",
                        "earthquakes_above_7.csv", 7.0)
expected_value = """\
id;location;impact;time
us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26
us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35
us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22
"""
assert(expected_value == read_file("earthquakes_above_7.csv"))
print("OK")
