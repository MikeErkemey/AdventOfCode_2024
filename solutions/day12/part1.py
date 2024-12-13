import time
from collections import deque
import sys

def solve(input):
    computedGardens = set()
    res = 0
    for i in  range(len(input)):
        for j in range(len(input[i])):
            if (j,i) not in computedGardens:
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

    xPer = 0
    yPer = 0
    for i in range(minX, maxX+1):
        t = False
        for j in range(minY, maxY+1):
            if (i,j) in garden:
                if not t:
                    xPer += 1
                t = True
            else:
                t = False
    for j in range(minY, maxY + 1):
        t = False
        for i in range(minX, maxX+1):
            if (i,j) in garden:
                if not t:
                    yPer += 1
                t = True
            else:
                t = False

    return (yPer*2 + xPer*2) * area

if __name__ == '__main__':
    with open("../../input/day12.txt") as file:
        input = [[c for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
