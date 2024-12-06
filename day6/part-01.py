# --- Day 6: Guard Gallivant ---

# Solution
import sys

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    grid = list(map(str.strip, f.readlines()))

nrows = len(grid)
ncols = len(grid[0])

def get_position():
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "^":
                return (r, c)
            
r, c = get_position()
dr, dc = -1, 0
visited = set()

while True:
    visited.add((r, c))
    if not (0 <= r+dr < nrows and 0 <= c+dc < ncols):
        # Maze ended
        break
    if grid[r+dr][c+dc] == "#":
        # turn 90 degree right
        dc, dr = -dr, dc
    else:
        r, c = r+dr, c+dc

count = len(visited)

print(count)
