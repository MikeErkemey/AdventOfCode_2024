import time
from collections import deque

def solve(input):
    q = deque()

    lookUp = dict()

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == 9:
                q.append((x, y))
                lookUp[(x, y)] = 1

    dir = [(-1,0),(1,0),(0,1),(0,-1)]

    while len(q) != 0:
        p = q.popleft()

        for d in dir:
            dp = (p[0]-d[0],p[1]-d[1])
            if 0 <= dp[0] < len(input) and 0 <= dp[1] < len(input[0]):
                if input[p[1]][p[0]]-1 == input[dp[1]][dp[0]]:
                    if dp in lookUp:
                        lookUp[dp] += lookUp[p]
                    else:
                        lookUp[dp] = lookUp[p]
                        q.append(dp)

    return sum(v for k,v in lookUp.items() if input[k[1]][k[0]] == 0)

if __name__ == '__main__':
    with open("../../input/day10.txt") as file:
        input = [[int(c) for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
