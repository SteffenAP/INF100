#Oppgave 1
def filter_high_temperatures(path_input, path_output, threshold_temp):
    f = open(path_input, "r", encoding = 'utf-8') #åpner fil i read med utf8
    output = open(path_output, "w", encoding = 'utf-8') #åpner output fil med write, lager fil
    input_content = f.read() #variabel for innhold i input
    for lines in input_content.splitlines(): #for hver linje i inputcontent
        if float(lines.split(" ")[1]) >= float(threshold_temp): #sjekker om temp er over eller lik threshold
            output.write(f"{lines}\n") #legger til temp i output

#Assert oppgave 1
print("Tester filter_high_temperatures... ", end="")
filter_high_temperatures("temperatures.txt", "high_temps.txt", 23.5)
expected_result = """\
Monday 23.5
Wednesday 24.0
Thursday 23.9
Sunday 23.9
"""
with open("high_temps.txt", "rt", encoding='utf-8') as f: 
    actual_result = f.read()
assert(expected_result == actual_result)
print("OK")

filter_high_temperatures("temperatures.txt", "high_temps.txt", 23.5)