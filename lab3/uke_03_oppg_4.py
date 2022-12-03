def cross_sum(n):
    cross = 0
    for number in str(n):
        cross += int(number)
    return cross

def nth_number_with_cross_sum_x(n, x):
    count = 0
    for number in range(x, 99999):
        if cross_sum(number) == x:
            count += 1
        if count == n: 
            return number
        
    
print("Tester nth_number_with_cross_sum_x... ", end="")
assert(7 == nth_number_with_cross_sum_x(1, 7))
assert(16 == nth_number_with_cross_sum_x(2, 7))
assert(25 == nth_number_with_cross_sum_x(3, 7))
assert(19 == nth_number_with_cross_sum_x(1, 10))
assert(28 == nth_number_with_cross_sum_x(2, 10))
assert(37 == nth_number_with_cross_sum_x(3, 10))
assert(2000 == nth_number_with_cross_sum_x(10, 2))
print("OK")

print("Tester cross_sum... ", end="")
assert(1 == cross_sum(1))
assert(3 == cross_sum(12))
assert(6 == cross_sum(123))
assert(10 == cross_sum(1234))
assert(10 == cross_sum(4321))
print("OK")
