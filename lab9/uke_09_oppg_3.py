import copy

def rotate(grid):
    rowsgrid = len(grid) #varabel for row length
    colgrid = len(grid[0]) #variabel for column length
    copiedgrid = [] # ny liste
    for _ in range(colgrid):
        copiedgrid.append([0] * rowsgrid) #lager en liste med filler variabler for passer formen til den ønskede listen
    for indexrow in range(rowsgrid): # for hver rad
        for indexcol in range(colgrid): # for hver kolonner
            copiedgrid[indexcol][indexrow] = grid[indexrow][indexcol] #setter inn variablen fra originale i motsatt posisjon i copiedgrid
    return copiedgrid

print("Tester rotate... ", end="")
# Test 1
a = [
    ["a", "c"],
    ["b", "d"]
]
assert([
    ["a", "b"],
    ["c", "d"],
] == rotate(a))

# Test 2
a = [
    [1, 4],
    [2, 5],
    [3, 6],
]
assert([
    [1, 2, 3],
    [4, 5, 6],
] == rotate(a))
# Sjekk at a ikke er mutert
assert([[1, 4], [2, 5], [3, 6]] == a)
print("OK")



