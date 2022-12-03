def weekly_pay(hourly_rate, hours):
    pay = 0
    if hours > 60: #Hvis mer enn 60 timer
        return "En ansatt jobber mer enn 60 timer"
    if hourly_rate < 200: #Under minstelønn
        return "Minstelønnskravet er ikke oppfylt"
    if hours > 40: #Hvis overtid
        overtime = hours - 40 #mengde overtid
        pay += 40 * hourly_rate #fast lønn
        pay += overtime * (hourly_rate * 1.5) #overtidlønn
        return pay
    else:
        pay += hours * hourly_rate #lønn
        return pay

#Assert
print("Tester weekly_pay... ", end="")
assert(10_000 == weekly_pay(1000, 10))
assert(40_000 == weekly_pay(1000, 40))
assert(20_000 == weekly_pay(500, 40))
assert(41_500 == weekly_pay(1000, 41))
assert(70_000 == weekly_pay(1000, 60))
assert("En ansatt jobber mer enn 60 timer" == weekly_pay(1000, 61))
assert("Minstelønnskravet er ikke oppfylt" == weekly_pay(100, 40))
print("OK")