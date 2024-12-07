import time


def solve(input):
    y, x = next((i, row.index('^')) for i, row in enumerate(input) if '^' in row)

    points = set()
    dir = (0,-1)

    while 0 <= x + dir[0] < len(input) and 0 <= y+dir[1] < len(input[0]):
        points.add((x,y))

        if input[y + dir[1]][x + dir[0]] == '#':
            dir = (-dir[1],dir[0])

        x += dir[0]
        y += dir[1]

    return len(points) + 1


if __name__ == '__main__':
    with open("../../input/day06.txt") as file:
        input = [[c for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")