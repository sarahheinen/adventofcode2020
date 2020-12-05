nums = open("day01Input.txt", "r")
fourDigitList = []
lessList = []

for line in nums.readlines():
    line = line.strip("\n")
    if len(line) < 4:
        lessList.append(int(line))
    else:
        fourDigitList.append(int(line))
    fourDigitList.sort()
    lessList.sort()

for num1 in fourDigitList:
    for num2 in lessList:
        if num1 + num2 == 2020:
            answer = num1 * num2

print(answer)