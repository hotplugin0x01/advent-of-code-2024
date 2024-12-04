# --- Day 4: Ceres Search ---
# URL: https://adventofcode.com/2024/day/4

# Solution
import sys
from collections import defaultdict

# if len(sys.argv) != 2:
#     print("[-] Please provide input file!")
#     sys.exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

directions = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            directions.append((dx, dy))

# print(directions)

char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, char in enumerate(row):
        char_map[char].add((r, c))

count = 0

for r, c in char_map['X']:
    for dr, dc in directions:
        for i, char in enumerate("MAS", 1):
            if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                break
        else:
            count +=1


print(count)
