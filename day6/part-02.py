
# Solution
import sys

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    grid = list(map(list, map(str.strip, f.readlines())))

nrows = len(grid)
ncols = len(grid[0])

def get_position():
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "^":
                return (r, c)

start_r, start_c = get_position()

def check_loop():
    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()

    while True:
        if (r, c, dr, dc) in visited:
            return True

        visited.add((r, c, dr, dc))
        if not (0 <= r+dr < nrows and 0 <= c+dc < ncols):
            # Maze ended
            return False
        if grid[r+dr][c+dc] == "#":
            # turn 90 degree right
            dc, dr = -dr, dc
        else:
            r, c = r+dr, c+dc

count = 0
for r in range(nrows):
    for c in range(ncols):
        if grid[r][c] != ".":
            continue
        # grid[r] = grid[r][:c] + "#" + grid[r][c+1:]
        grid[r][c] = '#'
        if check_loop():
            count +=1
        grid[r][c] = '.'
        # grid[r] = grid[r][:c] + "." + grid[r][c+1:]


print(count)
