import time


def search(input, x, y, dir, points, block):
    while 0 <= x + dir[0] < len(input) and 0 <= y+dir[1] < len(input[0]):
        if ((x, y) in points[dir]):
            return True
        points[dir].add((x, y))
        if input[y + dir[1]][x + dir[0]] == '#' or (block[1] == y + dir[1] and block[0] == x + dir[0]):
            return search(input, x, y, (-dir[1], dir[0]), points,block)
        x += dir[0]
        y += dir[1]

    return False


def solve(input):
    y, x = next((i, row.index('^')) for i, row in enumerate(input) if '^' in row)
    startY = y
    startX = x

    block = set()
    points = set()
    dir = (0,-1)

    while 0 <= x + dir[0] < len(input) and 0 <= y+dir[1] < len(input[0]):
        points.add((x,y))

        if input[y + dir[1]][x + dir[0]] == '#':
            dir = (-dir[1],dir[0])

        x += dir[0]
        y += dir[1]
    points.add((x,y))

    for p in points:
        if p[0] == startX and startY == p[1]:
            continue

        points2 = dict()
        points2[(0, 1)] = set()
        points2[(1, 0)] = set()
        points2[(0, -1)] = set()
        points2[(-1, 0)] = set()

        if search(input, startX, startY, (0,-1), points2, p):
            block.add(p)

    return len(block)


if __name__ == '__main__':
    with open("../../input/day06.txt") as file:
        input = [[c for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
