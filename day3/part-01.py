# --- Day 3: Mull It Over ---
# URL: https://adventofcode.com/2024/day/3

# Solution
import sys
import re

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip()

mul = lambda x, y: x * y

exp = re.findall("mul\(\d+,\d\)", lines)

result = sum(list(map(eval, exp)))

print(result)