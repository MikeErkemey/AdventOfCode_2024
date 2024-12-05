with open("../../input/day02.txt") as file:
    input = [line.rstrip() for line in file]


matrix = [list(map(int, x)) for x in (i.split() for i in input)]

print(matrix)

maxIncrease = 3
counter = 0
for level in matrix:
    higher = None
    holds = True
    for j in range(0, len(level)-1):
        if(higher == None):
            if level[j] < level[j+1]:
                higher = False
            else:
                higher = True
        if higher and level[j] <= level[j+1]:
            holds = False
            break
        if not higher and level[j] >= level[j+1]:
            holds = False
            break
        if abs(level[j] - level[j+1]) > 3:
            holds = False
            break
    if holds:
        counter += 1

print(counter)





