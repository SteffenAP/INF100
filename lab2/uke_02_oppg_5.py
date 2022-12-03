print("Enter a unit (nm or THz):")
inunit = input()
if inunit == "nm" or inunit == "Nm" or inunit == "NM":
    inunit = "nm"
elif inunit == "THz" or inunit == "THZ" or inunit == "thz" or inunit == "Thz":
    inunit = "THz"
else:
    print()
    print(("The unit must be either nm or Thz, it can not be " + inunit))
    quit()

print("Enter a value in " + inunit + ":")
invalue = int(input())

print()

def frequency_or_wavelength_to_color(inunit):
    if inunit == "nm":
        if wavelength_to_color(invalue) == None:
            return ("There is no color with wavelength " + str(invalue) + " nm")
        else:
            return wavelength_to_color(invalue)
    if inunit == "THz":
        if frequency_to_color(invalue) == None:
            return("There is no color with frequency " + str(invalue) + " THZ")
        else:
            return frequency_to_color(invalue)


def wavelength_to_color(x):
    if 380 <= x <= 450:
        return "Violet"
    elif 450 < x <= 485:
        return "Blue"
    elif 485 < x <= 500:
        return "Cyan"
    elif 500 < x <= 565:
        return "Green"
    elif 565 < x <= 590:
        return "Yellow"
    elif 590 < x <= 625:
        return "Orange"
    elif 625 < x <= 750:
        return "Red"
    else:
        return None

def frequency_to_color(y):
    c = (3e8)
    f = ((y)*1e12)
    m = c/f
    nm = ((m)*(1e9))
    return (wavelength_to_color(nm))

print(frequency_or_wavelength_to_color(inunit))

assert("Green" == wavelength_to_color(565))
assert("Violet" == wavelength_to_color(400))
assert(None == wavelength_to_color(6500))

assert("Cyan" == frequency_to_color(610))
assert("Red" == frequency_to_color(450))
assert(None == frequency_to_color(1.5e-2))
