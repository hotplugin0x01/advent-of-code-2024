# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# For these example lists, here is the process of finding the similarity score:

#     The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
#     The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
#     The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
#     The fourth number, 1, also does not appear in the right list.
#     The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
#     The last number, 3, appears in the right list three times; the similarity score again increases by 9.

# So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).



# Solution
import sys

if len(sys.argv) != 2:
    print("[-] Please provide input file!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

arr1 = []
arr2 = []

for line in lines:
    temp = list(map(int, line.strip().split()))
    arr1.append(temp[0])
    arr2.append(temp[1])

score = 0

for x in arr1:
    count = 0
    for y in arr2:
        if x == y:
            count += 1
    score += (x * count)

print(score)