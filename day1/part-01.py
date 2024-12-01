# --- Day 1: Historian Hysteria ---
# Link: https://adventofcode.com/2024/day/1
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# In the example list above, the pairs and distances would be as follows:
#     The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
#     The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
#     The third-smallest number in both lists is 3, so the distance between them is 0.
#     The next numbers to pair up are 3 and 4, a distance of 1.
#     The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
#     Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.

# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!


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

distance = 0
for x, y in zip(sorted(arr1), sorted(arr2)):
    distance += abs(x - y)


print(distance)