file = open("day03Input.txt", "r")

map = []
treeList = []

for line in file.readlines():
    map.append(line.rstrip("\n"))

for right in [1, 3, 5, 7]:
    trees = 0
    positionX = 0
    for y in range(1, len(map)):
        positionX = (positionX + right) % len(map[0])
        if map[y][positionX] == "#":
            trees = trees + 1
    treeList.append(trees)

trees = 0
positionX = 0
for y in range(2, len(map), 2):
    positionX = (positionX + 1) % len(map[0])
    if map[y][positionX] == "#":
        trees = trees + 1
treeList.append(trees)

answer = 1

for num in treeList:
    answer = answer * num

print(answer)