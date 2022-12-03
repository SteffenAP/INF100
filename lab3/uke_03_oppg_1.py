def multiples_of_seven_up_to(n):
    for number in range(1, n):
        if number % 7 == 0:
            print(number)
multiples_of_seven_up_to(49)