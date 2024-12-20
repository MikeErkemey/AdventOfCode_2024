import time
from collections import deque

def solve(input):

    m = []

    for i in range(len(input)):
        m.append([])
        for j in range(len(input[i])):
            if input[i][j] == 'S':
                sx,sy = j,i
            elif input[i][j] == 'E':
                ex,ey = j,i
            m[i].append(0)

    q = deque()
    q.append((sx,sy,0))
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = set()

    while q:
        cx,cy,cc = q.popleft()
        if (cx,cy) in visited:
            continue
        m[cy][cx] = cc
        visited.add((cx,cy))
        for d in dirs:
            dx,dy = d
            nx,ny = dx + cx, cy + dy
            if input[ny][nx] == '.':
                q.append((nx,ny,cc+1))

    ma = max([max(i) for i in m])
    m[ey][ex] = ma + 1
    res = 0

    for p in visited:
        cx,cy = p
        for d in dirs:
            dx,dy = d
            nx,ny = dx + cx, cy + dy
            if input[ny][nx] == '.':
                q.append((nx,ny))
            else:
                nx,ny = dx + nx, dy + ny
                if 0 <= ny < len(m) and 0 <= nx < len(m[0]) and input[ny][nx] != '#':
                    if m[ny][nx] - m[cy][cx] - 2 >= 100:
                        res += 1

    return res

if __name__ == '__main__':
    with open("../../input/day20.txt") as file:
        input = [[c for c in line.rstrip()] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
