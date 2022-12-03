import copy
#Oppgave 2 del A
def remove_row(grid, row):
    grid.remove(grid[row]) #Fjerner verdien

#Del B
def row_removed(grid, row):
    nondgrid = copy.deepcopy(grid) #Lager dypkopi av flerdimensjonal liste
    nondgrid.remove(nondgrid[row]) #Fjerner verdien
    return nondgrid  

#Del C
def remove_col(grid, col):
    for row in range(len(grid)):
        del grid[row-1][col] #Sletter kolonneindeks i hver rad

#Del D
def col_removed(grid, col):
    nondgrid = copy.deepcopy(grid) #Lager dypkopi av flerdimensjonal liste
    for row in range(len(nondgrid)):
        del nondgrid[row-1][col] #Sletter kolonneindeks i hver rad
    return nondgrid

#Assert Del A
print("Tester remove_row... ", end="")
# Test 1
grid = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ]
remove_row(grid, 0)
assert([
        [21, 22, 23],
        [31, 32, 33],
    ] == grid)

# Test 2
grid2 = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]
remove_row(grid2, 1)
assert([
        [11, 12, 13],
        [31, 32, 33],
    ] == grid2)
print("OK")


#Assert Del b
print("Tester row_removed... ", end="")
grid = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]

grid_without_row1 = row_removed(grid, 1)
assert([
        [11, 12, 13],
        [31, 32, 33],
    ] == grid_without_row1)
    
# Sjekk at vi ikke har mutert grid
assert([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ] == grid)

# Sjekk at grid_without_row1 ikke inneholder aliaser til grid
grid_without_row1[0][1] = 1212 # Muterer grid_without_row1
assert([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ] == grid)
print("OK")

#Assert del C
print("Tester remove_col... ", end="")
# Test 1
grid1 = [
        [16, 8, 3],
        [2, 10, 15],
    ]
remove_col(grid1, 0)
assert([
        [8, 3],
        [10, 15],
    ] == grid1)

# Test 2
grid2 = [
        [3, 0, 9],
        [4, 5, 3],
        [6, 8, 1],
    ]
remove_col(grid2, 1)
assert ([
        [3, 9],
        [4, 3],
        [6, 1],
    ] == grid2)
print("OK")

#Assert Del D
print("Tester col_removed... ", end="")
# Test 1
grid = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]
assert ([
        [12, 13],
        [22, 23],
        [32, 33],
    ] == col_removed(grid, 0))
# Sjekk at grid ikke ble mutert
assert([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ] == grid)

# Test 2
assert ([
        [11, 12],
        [21, 22],
        [31, 32],
    ]== col_removed(grid, 2))
print("OK")