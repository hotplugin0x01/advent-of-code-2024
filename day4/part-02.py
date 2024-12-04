
# Solution
import sys
from collections import defaultdict

# if len(sys.argv) != 2:
#     print("[-] Please provide input file!")
#     sys.exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, char in enumerate(row):
        char_map[char].add((r, c))



upleft = lambda r, c: (r - 1, c - 1)
upright = lambda r, c: (r - 1, c + 1)
downleft = lambda r, c: (r + 1, c - 1)
downright = lambda r, c: (r + 1, c + 1)
count = 0

for r, c in char_map['A']:
    if upleft(r, c) in char_map['M']:
        if downleft(r, c) in char_map['M'] and upright(r, c) in char_map['S'] and downright(r, c) in char_map['S']:
            count +=1
        elif upright(r,c) in char_map['M'] and downleft(r, c) in char_map['S'] and downright(r, c) in char_map['S']:
            count +=1
    elif downright(r, c) in char_map['M']:
        if downleft(r, c) in char_map['M'] and upright(r, c) in char_map['S'] and upleft(r, c) in char_map['S']:
            count +=1
        elif upright(r,c) in char_map['M'] and downleft(r, c) in char_map['S'] and upleft(r, c) in char_map['S']:
            count +=1

print(count)