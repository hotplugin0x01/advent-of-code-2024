
# Solution
import sys
import re

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip()

exp = re.findall("(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", lines)
# [('827', '465', ''), ('', '', "don't()"),  ('', '', 'do()')]

result = 0

enabled = True
for i in exp:
    if i[2] == "" and enabled:
        result += int(i[0]) * int(i[1])
    else:
        if i[2] == "do()":
            enabled = True
        else:
            enabled = False
 
print(result)