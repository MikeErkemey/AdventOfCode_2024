import time


def solve(input):
    matrix = input[:input.index('')]
    instructions = input[input.index('') + 1:]
    dirs = {'<' : (-1,0), 'v' : (0,1), '^' : (0,-1),'>' : (1,0)}
    points = dict()
    x = 0
    y = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '.':
                points[(j,i)] = matrix[i][j]
                if matrix[i][j] == '@':
                    y = i
                    x = j

    for dir in ''.join(instructions):
        (dx,dy) = dirs[dir]
        x2 = x + dx
        y2 = y + dy

        while (x2,y2) in points and points[(x2,y2)] != '#':
            x2 += dx
            y2 += dy

        if (x2,y2) not in points:
            while True:
                points[(x2,y2)] = points[(x2 - dx, y2 - dy)]
                x2 -= dx
                y2 -= dy
                if x2 == x and y2 == y:
                    points.pop((x,y))
                    x += dx
                    y += dy
                    break
    return sum([p[0] + p[1] * 100 for p in points if points[p] == 'O'])


if __name__ == '__main__':
    with open("../../input/day15.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
