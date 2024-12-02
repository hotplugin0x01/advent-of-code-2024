# --- Day 2: Red-Nosed Reports ---

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# This example data contains six reports each containing five levels.
#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.

# In the example above, the reports can be found safe or unsafe by checking those rules:

#     7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#     1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#     9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#     1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#     8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#     1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.


# Solution
# import sys

# if len(sys.argv) != 2:
#     print("[-] Please provide input file!")
#     sys.exit()

# with open(sys.argv[1], 'r') as f:
#     lines = f.readlines()

# reports = []
# for line in lines:
#     arr = list(map(int, line.strip().split()))
#     reports.append(arr)

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1

# count = 0
# for report in range(len(reports)):
#     f = True
#     inc = False
#     dec = False
#     safe = False
#     for level in range(len(reports[report])-1):
#         left = reports[report][level]
#         right = reports[report][level+1]

#         if abs(left-right) not in [1,2,3]:
#             safe = False
#             # unsafe
#             break
#         if f:
#             inc = left < right
#             dec = left > right
#             f = False
#             continue
        
#         if inc and left > right:
#             safe = False
#             break
#         if dec and  left < right:
#             safe = False
#             break

#         safe = True
     
#     if safe:
#         count +=1


# print(count)



# Anothe Solution
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

count = 0
for report in reports:
    inc_or_dec = (report == sorted(report) or report == sorted(report, reverse=True))
    safe = False
    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) not in range(1,4):
            safe = False
            break
        safe = True
    
    if safe and inc_or_dec:
        count += 1

print(count)