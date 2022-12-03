#Oppgave 3
def sort_by_sign(a):
    sorted_list = [ ]
    for index, value in enumerate(a):
        if value < 0:
            sorted_list.append(value)
    for index, value in enumerate(a):
        if value == 0:
            sorted_list.append(value)
    for index, value in enumerate(a):
        if value > 0:
            sorted_list.append(value)
    return sorted_list

#assert 3
print("Tester sort_by_sign... ", end="")
# Test 1
a = [3, -4, 1, 0, -1, 0, -2]
assert([-4, -1, -2, 0, 0, 3, 1] == sort_by_sign(a))

# Test 2
a = [10, -10, -2, 0, 0, 30, 10]
assert([-10, -2, 0, 0, 10, 30, 10] ==  sort_by_sign(a))

# Test 3
a = [100, -10, -20, 1000, -1000, 10]
assert([-10, -20, -1000, 100, 1000, 10] == sort_by_sign(a))
print("OK")