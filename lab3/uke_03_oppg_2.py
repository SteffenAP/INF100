def multiplication_table(n):
    for number in range (1, n+1):
        index = number
        print(str(number) + ":", end=" ")
        for number in range(1, n+1):
            print(index * number, end=" ")
        print()
multiplication_table(3)
multiplication_table(5)