import time
from collections import deque

def solve(input):
    res = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                res += dfs(input, j,i)
    return res

def dfs(input, x, y):
    stack = deque()
    stack.append((x,y))
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    visited = set()
    res = 0
    while len(stack) != 0:
        p = stack.pop()
        visited.add(p)

        if input[p[1]][p[0]] == 9:
            res += 1
            continue

        for d in dir:
            dp = (p[0]-d[0],p[1]-d[1])
            if 0 <= dp[0] < len(input) and 0 <= dp[1] < len(input[0]) and dp not in visited:
                if input[p[1]][p[0]]+1 == input[dp[1]][dp[0]]:
                    stack.append(p)
                    stack.append(dp)
                    break
    return res

if __name__ == '__main__':
    with open("../../input/day10.txt") as file:
        input = [[int(c) for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
