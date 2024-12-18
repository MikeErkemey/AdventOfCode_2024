import time
from collections import deque

def solve(input):
    input2 = input[:1024]
    matrix = []
    maxX = 70+1
    maxY = 70+1

    for yi in range(maxY):
        matrix.append([])
        for xi in range(maxX):
            if [xi,yi] in input2:
                matrix[yi].append('#')
            else:
                matrix[yi].append('.')

    i = 1024
    path = findPath(matrix)
    while path is not None:
        x,y = input[i]
        matrix[y][x] = '#'
        if (x,y) in path:
            path = findPath(matrix)
        i+=1
    return ','.join(str(x) for x in input[i-1])


def findPath(matrix):
    maxX = 70+1
    maxY = 70+1
    x = 0
    y = 0
    paths = dict()
    visited = set()
    q = deque()
    q.append((x,y))
    dirs = [(1,0),(0,-1),(0,1),(-1,0)]
    while q:
        x,y = q.popleft()
        if (x,y) in visited:
            continue
        if x == maxX-1 and y == maxY-1:
            path = set()
            path.add((x,y))
            while x != 0 or y != 0:
                (x,y) = paths[(x,y)]
                path.add((x,y))
            return path

        visited.add((x,y))

        for d in dirs:
            dx,dy = d
            x2 = dx + x
            y2 = dy + y
            if 0 <= x2 < maxX and 0 <= y2 < maxY and (x2,y2) not in visited and matrix[y2][x2] != '#':
                paths[(x2,y2)] = (x,y)
                q.append((x2,y2))
    return None


if __name__ == '__main__':
    with open("../../input/day18.txt") as file:
        input = [[int(x) for x in line.rstrip().split(",")] for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
