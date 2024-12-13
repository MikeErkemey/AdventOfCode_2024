import time
from collections import deque
import sys


def solve(input):
    computedGardens = set()
    res = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (j, i) not in computedGardens:
                garden = getGarden(computedGardens, j, i, input, input[i][j])
                res += computeGarden(garden)

    return res

def getGarden(computedGardens, x,y, input, type):
    q = deque()
    q.append((x, y))
    garden = set()

    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while len(q) != 0:
        p = q.popleft()

        if p in garden:
            continue

        garden.add(p)
        computedGardens.add(p)

        for d in dirs:
            dp = (p[0] - d[0], p[1] - d[1])
            if 0 <= dp[0] < len(input[0]) and 0 <= dp[1] < len(input):
                if input[dp[1]][dp[0]] == type:
                    q.append(dp)

    return garden

def computeGarden(garden) -> int:
    minX, maxX = (f(x[0] for x in garden) for f in (min, max))
    minY, maxY = (f(x[1] for x in garden) for f in (min, max))


    area = len(garden)

    xUp = 0
    vis = set()
    for i in range(minX, maxX + 1):
        outside = False
        for j in range(minY, maxY + 1):
            p = (i,j)
            if p in garden:
                if p in vis:
                    outside = True
                    continue
                vis.add(p)
                if not outside:
                    xUp += 1
                    for k in range(i+1, maxX + 1):
                        if (k, j) in garden and not((k, j - 1) in garden):
                            vis.add((k, j))
                        else:
                            break
                outside = True
            else:
                outside = False

    xDown = 0
    vis = set()
    for i in range(minX, maxX + 1):
        outside = False
        for j in range(maxY, minY-1, -1):
            p = (i, j)
            if p in garden:
                if p in vis:
                    outside = True
                    continue
                vis.add(p)
                if not outside:
                    xDown += 1
                    for k in range(i+1, maxX + 1):
                        if (k, j) in garden and not((k, j + 1) in garden):
                            vis.add((k, j))
                        else:
                            break
                outside = True
            else:
                outside = False
    yLeft = 0
    vis = set()
    for j in range(minY, maxY + 1):
        outside = False
        for i in range(minX, maxX + 1):
            p = (i, j)
            if p in garden:
                if p in vis:
                    outside = True
                    continue
                vis.add(p)
                if not outside:
                    yLeft += 1
                    for k in range(j+1, maxY + 1):
                        if (i, k) in garden and not((i-1, k) in garden):
                            vis.add((i, k))
                        else:
                            break
                outside = True
            else:
                outside = False

    yRight = 0
    vis = set()
    for j in range(minY, maxY + 1):
        outside = False
        for i in range(maxX,minX-1,-1):
            p = (i, j)
            if p in garden:
                if p in vis:
                    outside = True
                    continue
                vis.add(p)
                if not outside:
                    yRight += 1
                    for k in range(j+1, maxY+1):
                        if (i, k) in garden and not((i+1, k) in garden):
                            vis.add((i, k))
                        else:
                            break
                outside = True
            else:
                outside = False
    return (xUp + xDown + yLeft + yRight) * area


if __name__ == '__main__':
    with open("../../input/day12.txt") as file:
        input = [[c for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
