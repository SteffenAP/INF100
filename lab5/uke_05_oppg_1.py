#1a, sletter elementer fra a med remove
def remove_threes(a):
    while 3 in a:
        a.remove(3)

#1b, lager en "running count" liste for å bare hente ut hver fjerde verdi
def every_fourth(a):
    total_list = []
    total_list = [a[index] for index  in range(len(a)) if index % 4 == 0]
    return total_list


#1c, lager en alias, skiller den til å være de delte verdiene
#Sjekker om en verdi i den nye listen er et heltall og konverterer de til en int
#fjerner første tall i a i hver iterasjon av løkken for å tømme a helt
#legger til b i a
def halve_values(a):
    b = a
    b = [(b[index]*0.5) for index  in range(len(b))]
    for index, value in enumerate(b):
        if value % 1 == 0:
            b[index] = int(value)
        a.remove(a[0])
    a.extend(b)


#1d
#lager en liste som henter unike verdier ved å sjekke om de allerede er tilstede i listen
def unique_values(a):
    unique_list = []
    for index, value in enumerate(a):
        if a[index] not in unique_list:
            unique_list.append(a[index])
    return unique_list


#1e
#legger til matchende b i hver a
def add_list(a, b):
    for index in range(len(a)):
        a[index] += b[index]



#Assert 1a
print("Tester remove_threes... ", end="")
# Test 1
a = [1, 2, 3, 4]
remove_threes(a)
assert(a == [1, 2, 4])

# Test 2
a = [1, 2, 3, 3]
remove_threes(a)
assert(a == [1, 2])

# Test 3
a = [3, 3, 1, 3, 2, 4, 3, 3, 3]
remove_threes(a)
assert(a == [1, 2, 4])

# Test 4
a = [3, 3]
remove_threes(a)
assert(a == [])
print("OK")

#Assert 1b

print("Tester every_fourth... ", end="")
# Test 1
a = ["a", "b", "c", "d", "e"]
assert(["a", "e"] == every_fourth(a))
assert(["a", "b", "c", "d", "e"] == a)

# Test 2
a = list(range(10))
assert([0, 4, 8] == every_fourth(a))
assert(list(range(10)) == a)

# Test 3
a = list(range(20, 1000))
assert(list(range(20, 1000, 4)) == every_fourth(a))
assert(list(range(20, 1000)) == a)
print("OK")

#Assert 1c

print("Tester halve_values... ", end="")
a = [1, 2, 3]
halve_values(a)
assert([0.5, 1, 1.5] == a)
print("OK")

#Assert 1d

print("Tester unique_values... ", end="")
# Test 1
a = [1, 1, 2, 1, 3, 3, 3, 2]
assert([1, 2, 3] == unique_values(a))
assert([1, 1, 2, 1, 3, 3, 3, 2] == a)

# Test 2
a = ["a", "b", "c"]
assert(["a", "b", "c"] == unique_values(a))
assert(["a", "b", "c"] == a)
print("OK")

#assert 1e

print("Tester add_list... ", end="")
a = [1, 2, 3]
b = [4, 2, -3]
add_list(a, b)
assert([5, 4, 0] == a)
assert([4, 2, -3] == b)
print("OK")