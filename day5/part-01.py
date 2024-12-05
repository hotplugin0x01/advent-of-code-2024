# --- Day 5: Print Queue ---

# Solution
import sys
from collections import defaultdict

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
                return 0
    return job[len(job)//2]

count = 0
for job in jobs:
    count += check_job(job)


print(count)