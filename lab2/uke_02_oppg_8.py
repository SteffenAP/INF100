import math

def point_in_rectangle(x0, y0, x1, y1, x2, y2):
    if (x0 <= x2 <= x1 or x0 >= x2 >= x1) and (y0 <= y2 <= y1 or y0 >= y2 >= y1):
        return True
    else:
        return False

def rectangles_overlap(x0, y0, x1, y1, x2, y2, x4, y4):
    if ((max(x0, x1) >= x2 >= min(x0, x1)) or (max(x0, x1) >= x4 >= min(x0, x1))) and ((max(y0, y1) >= y2 >= min(x0, x1)) or (max(x0, x1) >= y4 >= min(x0, x1))):
        return True
    else:
        return False

def distance(x1, y1, x2, y2):
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

def circle_overlaps_rectangle(x0, y0, x1, y1, x2, y2, r2):
    r = r2
    if point_in_rectangle(x0, y0, x1, y1, x2, y2) == True:
        return True
    elif ((distance(x0, y0, x2, y2) <=  r) or (distance(x1, y1, x2, y2) <=  r)) or ((distance(x0, y1, x2, y2) <=  r) or (distance(x1, y0, x2, y2) <=  r)):
        return True
    elif ((max(x0, x1) >= (x2 - r)) and (min(y0, y1) <= y2 <= max(y0, y1))) or ((min(x0, x1) >= (x2 + r)) and (min(y0, y1) <= y2 <= max(y0, y1))):
        return True
    elif ((max(y0, y1) >= (y2 - r)) and (min(x0, x1) <= x2 <= max(x0, x1))) or ((min(y0, y1) >= (y2 + r)) and (min(x0, x1) <= x2 <= max(x0, x1))):
        return True
    else:
        return False

print("Tester point_in_rectangle... ", end="")
assert(point_in_rectangle(0, 0, 5, 5, 3, 3)) # Midt i
assert(point_in_rectangle(0, 5, 5, 0, 5, 3)) # På kanten
assert(not point_in_rectangle(0, 0, 5, 5, 6, 3)) # Utenfor
print("OK")

print("Tester rectangles_overlap... ", end="")
assert(rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6)) # Delvis overlapp
assert(rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4)) # Fullstendig overlapp
assert(rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7)) # Kryssende rektangler
assert(rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7)) # Deler et hjørne
assert(not rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8)) # Utenfor
print("OK")

print("Tester circle_overlaps_rectangle... ", end="")
assert(circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2)) # sirkel i midten
assert(not circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2)) # langt utenfor
assert(circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5)) # på hjørnet
assert(not circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5)) # akkurat ikke
assert(circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01)) # langs kanten
print("OK")

