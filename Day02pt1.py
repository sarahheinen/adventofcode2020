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
    counter = 0
    for letter in passwordList[index]:
        if letterList[index] == letter:
            counter = counter + 1
    if counter >= int(rangeList[index][0]) and counter <= int(rangeList[index][1]):
        validPasswords = validPasswords + 1

print(validPasswords)