import time
import re


def solve(input):
    maxX = 101
    maxY = 103
    points = []

    for i in input:
        match = re.findall("-?\d+", i)
        x,y = int(match[0]),int(match[1])
        dx,dy = int(match[2]),int(match[3])

        for _ in range(100):
            x = (x + dx) % maxX
            y = (y + dy) % maxY
        points.append((x,y))

    q1 = len([p for p in points if p[0] < maxX // 2 and p[1] < maxY // 2])
    q2 = len([p for p in points if p[0] > maxX // 2 and p[1] < maxY // 2])
    q3 = len([p for p in points if p[0] < maxX // 2 and p[1] > maxY // 2])
    q4 = len([p for p in points if p[0] > maxX // 2 and p[1] > maxY // 2])
    return q1 * q2 * q3 * q4


if __name__ == '__main__':
    with open("../../input/day14.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
