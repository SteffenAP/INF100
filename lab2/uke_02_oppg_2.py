def is_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 == 0):
        return True
    else:
        return False
print("Tester is_leap_year... ", end="")
assert(is_leap_year(1996))      # Forventer True
assert(not is_leap_year(1900))  # Forventer False
assert(is_leap_year(2000))      # Forventer True
print("OK")
