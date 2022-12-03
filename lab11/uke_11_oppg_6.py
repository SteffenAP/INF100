def add_numbers():
    inputval = 0
    sum = 0
    while inputval != "q":
        inputval = input("Give me an integer, press 'q' to quit: ")
        try:
            sum += int(inputval)
        except:
            if inputval != "q":
                print("That was not an integer, please try again")
            continue
    print(sum)

add_numbers()