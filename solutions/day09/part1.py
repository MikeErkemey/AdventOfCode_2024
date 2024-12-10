import time
from collections import deque

def solve(input):
    free = False
    freeSpaces = deque()
    ids = deque()
    indexSpace = 0
    id = 0
    for c in input:
        for i in range(int(c)):
            if not free:
                ids.append(id)
            else:
                freeSpaces.append(indexSpace)
            indexSpace += 1
        free = not free
        if not free:
            id += 1

    curIndex = 0
    sum = 0
    while len(freeSpaces) != 0 and len(ids) != 0:
        freeSpace = freeSpaces.popleft()
        for i in range(curIndex, freeSpace):
            if len(ids) == 0:
                break
            t = ids.popleft()
            sum += t * curIndex
            curIndex += 1
        if len(ids) == 0:
            break
        h = ids.pop()
        sum += h * freeSpace
        curIndex = freeSpace +1


    return sum


if __name__ == '__main__':
    with open("../../input/day09.txt") as file:
        input = [line.rstrip() for line in file][0]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
