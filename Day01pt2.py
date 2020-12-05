from itertools import product
nums = open("day01Input.txt", "r")
numList = []

for line in nums.readlines():
    line = line.strip("\n")
    numList.append(int(line))

for a, b, c in product(numList, repeat = 3):
    if a + b + c == 2020:
        answer = a * b * c

print(answer)