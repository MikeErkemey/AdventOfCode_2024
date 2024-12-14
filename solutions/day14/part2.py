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
        points.append((x,y,dx,dy))

    countIndex = 0
    for j in range(10403):
        for i in range(len(points)):
            p = points[i]
            points[i] = ((p[0] + p[2]) % maxX, (p[1] + p[3]) % maxY, p[2], p[3])
        # print(len([p for p in points if 40 < p[0] < 74]))
        # print(len([p for p in points if 19 < p[0] < 52]))
        if len([p for p in points if 19 < p[1] < 52]) == 350 and len([p for p in points if 40 < p[0] < 74]) == 361:
            countIndex = j
        if countIndex != 0:
            printTree(maxX, maxY, points)
            break

    return countIndex+1


def printTree(maxX, maxY, points):
    p = [(x,y) for x,y,dx,dy in points]

    for y in range(maxY):
        for x in range(maxX):
            if (x,y) in p:
                print("#", end='')
            else:
                print(".", end='')
        print("")

if __name__ == '__main__':
    with open("../../input/day14.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
