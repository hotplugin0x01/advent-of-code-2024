

# Solution
import sys

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

reports = []
for line in lines:
    arr = list(map(int, line.strip().split()))
    reports.append(arr)


def is_safe(report):
    safe = True
    inc_or_dec = (report == sorted(report) or report == sorted(report, reverse=True))
    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) not in range(1,4):
            safe = False
            break
    return inc_or_dec and safe


count = 0
for report in reports:
    safe = False
    for j in range(len(report)):
        # New arr without number
        arr = report[:j] + report[j+1:]
        if is_safe(arr):
            safe = True
    
    if safe:
        count += 1


print(count)