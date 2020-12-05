passwords = open("day02Input.txt", "r")

rangeList = []
letterList = []
passwordList = []

validPasswords = 0

for line in passwords.readlines():
    line = line.split()
    rangeNum = line[0].split("-")
    rangeList.append(rangeNum)
    letterList.append(line[1].strip(":"))
    passwordList.append(line[2])

for index in range(0, len(passwordList)):
    position1 = int(rangeList[index][0]) - 1
    position2 = int(rangeList[index][1]) - 1
    if (passwordList[index][position1] == letterList[index]) != (passwordList[index][position2] == letterList[index]):
        validPasswords = validPasswords + 1

print(validPasswords)