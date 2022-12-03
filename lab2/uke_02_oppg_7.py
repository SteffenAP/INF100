def is_legal_triangel(x1, x2, x3):
    if type(x1) == str or type(x2) == str or type(x3) == str:
        return False
    elif x1 + x2 <= x3:
        return False
    elif x1 + x3 <= x2:
        return False
    elif x2 + x3 <= x1:
        return False
    else:
        return True
print("Tester is_legal_triangel... ", end="")
assert(is_legal_triangel(2, 2, 3)) # True, dette er en mulig trekant
assert(not is_legal_triangel(3, 2, 1)) # False (1 + 2 er ikke større enn 3)
assert(not is_legal_triangel("2", "2", "3")) # False (dette er ikke tall)
print("OK")