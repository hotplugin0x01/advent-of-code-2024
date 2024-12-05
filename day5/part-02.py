
# Solution
import sys
from collections import defaultdict
from functools import cmp_to_key

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    data = f.read()

rules, jobs = data.split("\n\n")
rules = [tuple(map(int, line.split('|'))) for line in rules.splitlines()]
jobs = [tuple(map(int, line.split(','))) for line in jobs.splitlines()]

invalid_map = defaultdict(bool)

for x, y in rules:
    invalid_map[(y, x)] = True

def check_job(job):
    for i in range(len(job)):
        for j in range(i+1, len(job)):
            if invalid_map[(job[i], job[j])]:
                return False
    return True

def sort_job(a, b):
    if invalid_map[(a, b)]:
        return 1
    return -1

count = 0
for job in jobs:
    if not check_job(job):
        fixed = sorted(job, key=cmp_to_key(sort_job))
        count += fixed[len(fixed)//2]


print(count)