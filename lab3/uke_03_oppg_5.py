def split_line(x_lo, x_hi, n):
    increment = (x_hi - x_lo) / n
    for value in range (n):
        print(x_lo, end=" ")
        print(x_lo + increment, end=" ")
        print()
        x_lo += increment
    

split_line(1.0, 7.0, 3)
split_line(0.0, 1.0, 4)