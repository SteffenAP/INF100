#Oppgave 3
def all_rows_and_cols_equal_sum(grid):
    sumcol = 0
    sumrow = 0
    baserow = 0
    basecol = 0
    for row in range(len(grid)): # for hver rad
        for col in range(len(grid[0])): #hver kolonne i raden
            sumrow += grid[row-1][col-1] #legger sammen alle tall i rad
        if row == 0:
            baserow += sumrow #etablerer en baseverdi
            sumrow = 0
            continue
        if sumrow != baserow: #hvis videre iterasjoner er ulik baseverdien, er ikke alle rader like
            return False
        sumrow = 0
    for col in range(len(grid[0])): #samme som forrige, bare motsatt
        for row in range(len(grid)):
            sumcol += grid[row-1][col-1]
        if col == 0:
            basecol += sumcol
            sumcol = 0
            continue
        if sumcol != basecol:
            return False
        sumcol = 0
    return True

#Assert oppgave 3
print("Tester all_rows_and_cols_equal_sum... ", end="")
# Test 1
assert(all_rows_and_cols_equal_sum([
        [16, 8, 3],     # begge rader summerer til 27
        [2, 10, 15],    # alle kolonner summerer til 18
    ]))
    
# Test 2
assert(not all_rows_and_cols_equal_sum([
        [3, 0, 9],   # rad0 summerer til 12, col0 summerer til 13
        [4, 5, 3],   # rad1 summerer til 12, col1 summerer til 13
        [6, 8, 1],   # rad2 summerer til 15, col2 summerer til 13
    ]))

# Test 3
assert(not all_rows_and_cols_equal_sum([
        [3, 4, 6],   # rad0 summerer til 13, col0 summerer til 12
        [0, 5, 8],   # rad1 summerer til 13, col1 summerer til 12
        [9, 3, 1],   # rad2 summerer til 13, col2 summerer til 15
    ]))

# Test 3
assert (all_rows_and_cols_equal_sum([
        [1, 2, 3, 4], # alle rader og kolonner summerer til 10
        [2, 3, 4, 1],
        [3, 4, 1, 2],
        [4, 1, 2, 3],
    ]))
print("OK")
