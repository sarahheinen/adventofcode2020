file = open("day03Input.txt", "r")

map = []
positionX = 0
trees = 0

for line in file.readlines():
    map.append(line.rstrip("\n"))

for y in range(1, len(map)):
    positionX = (positionX + 3) % len(map[0])
    if map[y][positionX] == "#":
        trees = trees + 1

print(trees)