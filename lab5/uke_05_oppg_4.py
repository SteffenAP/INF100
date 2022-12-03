#Oppgave 4

def read_and_sort():
    sorted_list = [ ]
    ui = ""
    while ui != '0':
        ui = input()
        if ui != '0':
            sorted_list.append(ui)
    sorted_list = list(map(int, sorted_list))
    sorted_list.sort()
    for i in range(len(sorted_list)):
        print(sorted_list[i])

read_and_sort()
