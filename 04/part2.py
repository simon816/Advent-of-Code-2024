import sys

grid = []
for line in sys.stdin.readlines():
    grid.append(line.strip())

shapes = {
    'M.S.A.M.S',
    'S.S.A.M.M',
    'M.M.A.S.S',
    'S.M.A.S.M'
}

total = 0
for r, row in enumerate(grid):
    for c, letter in enumerate(row):
        if r < len(grid) - 2 and c < len(row) - 2:
            mini = list(grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3])
            mini[1] = mini[3] = mini[5] = mini[7] = '.'
            mini = ''.join(mini)
            if mini in shapes:
                total += 1
print(total)
