def g(x):
    return (((1/8)*(x*x)) - (2 * x) + (10))

def approx_area_under_g(x_lo, x_hi):
    x_i = 0
    for value in range(x_lo, x_hi):
        x_i += g(value)
    return x_i

def split_line(x_lo, x_hi, n):
    increment = (x_hi - x_lo) / n
    for value in range (n):
        print(x_lo, end=" ")
        print((x_lo + increment))
        x_lo += increment
        x_hi += increment

def riemann_sum_g(x_lo, x_hi, n):
    x_i = 0
    increment = (x_hi - x_lo) / n
    for value in range(n):
        if x_lo + (increment * value) < x_hi:
            x_i += (g(x_lo + (value * increment)) * increment)
    return x_i

def riemann_sum(f, x_lo, x_hi, n):
    x_i = 0
    increment = (x_hi - x_lo) / n
    for value in range(n):
        if x_lo + (increment * value) < x_hi:
            x_i += (f(x_lo + (value * increment)) * increment)
    return x_i 

def almost_equals(a, b):
    return abs(a - b) < 0.0000001
print("Tester g... ", end="")
assert(almost_equals(2.0, g(8.0)))
assert(almost_equals(4.0, g(4.0)))
assert(almost_equals(10.0, g(0.0)))
print("OK")

print("Tester approx_area_under_g... ", end="")
assert(4.0 == approx_area_under_g(4, 5))   # g(4)
assert(3.125 == approx_area_under_g(5, 6)) # g(5)
assert(7.125 == approx_area_under_g(4, 6)) # g(4) + g(5)
assert(23.75 == approx_area_under_g(1, 5)) # g(1) + g(2) + g(3) + g(4)
print("OK")

print("Tester riemann_sum_g... ", end="")
assert(almost_equals(7.125, riemann_sum_g(4, 6, 2)))
assert(almost_equals(6.71875, riemann_sum_g(4, 6, 4)))
assert(almost_equals(6.3348335, riemann_sum_g(4, 6, 1000)))

assert(almost_equals(23.75, riemann_sum_g(1, 5, 4)))
assert(almost_equals(22.4375, riemann_sum_g(1, 5, 8)))
assert(almost_equals(21.166676666, riemann_sum_g(1, 5, 1_000_000)))
print("OK")

# Vi sjekker først at riemann_sum med funksjonen g som argument gir
# samme svar som riemann_sum_g -metoden fra forrige deloppgave.
print("Tester riemann_sum med funksjonen g... ", end="")
assert(almost_equals(7.125, riemann_sum(g, 4, 6, 2)))
assert(almost_equals(6.71875, riemann_sum(g, 4, 6, 4)))
assert(almost_equals(6.3348335, riemann_sum(g, 4, 6, 1000)))

assert(almost_equals(23.75, riemann_sum(g, 1, 5, 4)))
assert(almost_equals(22.4375, riemann_sum(g, 1, 5, 8)))
assert(almost_equals(21.166676666, riemann_sum(g, 1, 5, 1_000_000)))
print("OK")

# Så tester vi med et par andre funksjoner
# Funksjonen som kvadrerer, square(x) = x**2
def square(x):
    return x**2

## Arealet under grafen square(x) = x**2 mellom 1 og 3
## Eksakt svar  er 8 + 2/3, altså 8.66666666....
## Merk at vi kommer gradvis nærmere eksakt svar ved å øke n
print("Tester riemann_sum med funksjonen square... ", end="")
assert(almost_equals(5.0, riemann_sum(square, 1, 3, 2)))
assert(almost_equals(7.88, riemann_sum(square, 1, 3, 10)))
assert(almost_equals(8.5868, riemann_sum(square, 1, 3, 100)))
print("OK")

# Funksjonen som er en jevnt stigende, linear(x) = x
def linear(x):
    return x

## Arealet under grafen for funksjonen f(x) = x mellom 2 og 4
## Eksakt svar er 6.
## Merk at vi kommer gradvis nærmere riktig svar ved å øke n
print("Tester riemann_sum med funksjonen linear... ", end="")
assert(almost_equals(5.0, riemann_sum(linear, 2, 4, 2)))
assert(almost_equals(5.5, riemann_sum(linear, 2, 4, 4)))
assert(almost_equals(5.998046875, riemann_sum(linear, 2, 4, 1024)))
print("OK")