def is_even_positive_int(x):
    if type(x) == str:
        return False
    elif x > 0 and (x % 2 == 0):
        return True
    else:
        return False
print("Tester is_even_positive_int...", end="")
assert(is_even_positive_int(123456)) # True, dette er et positivt partall
assert(not is_even_positive_int(-2)) # False (er ikke positivt)
assert(not is_even_positive_int(123)) # False (er ikke et partall)
assert(not is_even_positive_int("huffda")) # False (er ikke en int)
print("OK")

