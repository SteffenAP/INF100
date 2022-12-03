def human_to_dog_years(x):
    if x <= 2:
        return 10.5 * x
    else:
         return ((4 * (x-2)) + 21)

def almost_equals(a, b):
    return abs(a - b) < 0.00000001

print("Tester human_to_dog_years... ", end="")
assert(almost_equals(15.75, human_to_dog_years(1.5)))
assert(almost_equals(21.00, human_to_dog_years(2)))
assert(almost_equals(57.00, human_to_dog_years(11)))
print("OK")