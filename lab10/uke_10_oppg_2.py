#Oppgave 2
def num_pairwise_diff_gt10(a):
    diffctr = 0 #teller
    for index, number in enumerate(a): #henter index og tall fra liste
        if index == 0: #ignorerer første tilfelle
            continue
        if (number - 10) > a[index - 1]: # sjekker om tallet før er mer enn 10 mindre
            diffctr += 1
        elif (number + 10) < a[index - 1]: #sjekker om tallet før er mer enn 10 høyere
            diffctr += 1
    return diffctr #returnerer teller


#Assert oppgave 2
print("Tester num_pairwise_diff_gt10... ", end="")
a =[9, 3, 12, 0,- 3, 2, -9]  # Forskjellen er større: 12 -> 0 og 2 -> -9
assert(2 == num_pairwise_diff_gt10(a))
a =[10, 2, 12, 0, 1, 2, 11]
assert(1 == num_pairwise_diff_gt10(a))
a= [1, 14, 0, 12, 1, 20, 8]
assert(6 == num_pairwise_diff_gt10(a))
print("OK")