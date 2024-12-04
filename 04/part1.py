import sys

grid = []
for line in sys.stdin.readlines():
    grid.append(line.strip())

total = 0
for r, row in enumerate(grid):
    for c, letter in enumerate(row):
        if letter == 'X':
            if row[c:c+4] == 'XMAS':
                total += 1
            if c >= 3 and row[c-3:c+1] == 'SAMX':
                total += 1
            if r >= 3 and grid[r-1][c]+grid[r-2][c]+grid[r-3][c] == 'MAS':
                total += 1
            if r < len(grid) - 3 and grid[r+1][c]+grid[r+2][c]+grid[r+3][c] == 'MAS':
                total += 1
            if r < len(grid) - 3 and c < len(row) - 3 \
               and grid[r+1][c+1]+grid[r+2][c+2]+grid[r+3][c+3] == 'MAS':
                total += 1
            if r >= 3 and c >= 3 \
               and grid[r-1][c-1]+grid[r-2][c-2]+grid[r-3][c-3] == 'MAS':
                total += 1
            if r >= 3 and c < len(row) - 3 \
               and grid[r-1][c+1]+grid[r-2][c+2]+grid[r-3][c+3] == 'MAS':
                total += 1
            if r < len(grid) - 3 and c >= 3 \
               and grid[r+1][c-1]+grid[r+2][c-2]+grid[r+3][c-3] == 'MAS':
                total += 1
print(total)
