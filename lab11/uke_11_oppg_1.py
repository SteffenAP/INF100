#Oppgave 1
def dot_product(a, b):
    total = 0 #totalsum variabel
    for index in range(len(a)): #for hvert tall i listen
        total += (a[index] * b[index]) #legger til ai ganger bi i totalsum
    return total

#Assert oppgave 1
print("Tester dot_product... ", end="")

assert(32 == dot_product([1, 2, 3], [4, 5, 6]))
assert(12 == dot_product([0, 6, 1], [400, 1, 6]))
assert(657 == dot_product([43, 6, 1], [15, 1, 6]))

print("OK")