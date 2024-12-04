def check(level, x, y, asc, pardon):

    if y >= len(level):
        return True

    if abs(level[x] - level[y]) > 3:
        if pardon:
            return check(level, x, y + 1, asc, False)
        else:
            return False

    if asc and level[x] >= level[y]:
        if pardon:
            return check(level, x, y + 1, asc, False)
        else:
            return False

    if not asc and level[x] <= level[y]:
        if pardon:
            return check(level, x, y + 1, asc, False)
        else:
            return False

    if pardon:
        return check(level, y, y + 1, asc, True) or check(level, x, y + 1, asc, False)

    return check(level, y, y + 1, asc, False)


with open("../../input/day02.txt") as file:
    input = [line.rstrip() for line in file]


matrix = [list(map(int, x)) for x in (i.split() for i in input)]

print(matrix)

counter = 0

for i in matrix:
    if check(i,0,1,i[0] < i[1],True) or check(i,0,2,i[0] < i[2],False)or check(i,1,2,i[1] < i[2],False):
        print(i, "good")
        counter += 1
    else:
        print(i, "bad")
print(counter)





