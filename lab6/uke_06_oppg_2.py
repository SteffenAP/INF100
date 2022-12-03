#Oppgave 2
def alternate_sign_sum(a):
    total = 0 #total for summering
    for i in range(len(a)):
        if i % 2 == 0: #addisjon av partallsindekser
            total += a[i]
            continue
        else: #subtraksjon av oddetallsindekser
            total -= a[i]
    return total

#assert oppgave 2
assert(3 == alternate_sign_sum([1, 2, 3, 4, 5]))
assert(30 == alternate_sign_sum([10, 20, 30, 40, 50]))

a = [-10, 20, -30, 40, -50]
assert(-150 == alternate_sign_sum([-10, 20, -30, 40, -50]))
assert([-10, 20, -30, 40, -50] == a) # Sjekker at funksjonen ikke er destruktiv
print("OK")