with open("../../input/day06.txt") as file:
    input = [[c for c in line.rstrip()] for line in file]

y, x = next((i, row.index('^')) for i, row in enumerate(input) if '^' in row)

points = set()
dir = (0,-1)

while 0 <= x + dir[0] < len(input) and 0 <= y+dir[1] < len(input[0]):
    points.add((x,y))

    if input[y + dir[1]][x + dir[0]] == '#':
        dir = (-dir[1],dir[0])

    x += dir[0]
    y += dir[1]

print(len(points)+1)
