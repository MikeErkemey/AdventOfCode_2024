import time
from collections import deque

def solve(input):
    free = False
    freeSpaces = dict()
    ids = []
    indexSpace = 0
    id = 0
    for c in input:
        block = int(c)
        if not free:
            ids.append((block,indexSpace))
        elif block != 0:
            freeSpaces[indexSpace+block-1] = indexSpace
        indexSpace += block
        free = not free
        if not free:
            id += 1
    sum = 0
    changed = set()

    for i in range(len(ids)-1, -1,-1):
        if i in changed:
            continue
        for end,start in freeSpaces.items():
            if ids[i][1] < start:
                break
            block = end-start+1
            if block >= ids[i][0]:
                if start+ids[i][0] > end:
                    freeSpaces.pop(end)
                else:
                    freeSpaces[end] = start+ids[i][0]
                (l,r) = ids[i]
                r2 = l+r-1
                while r2+1 in freeSpaces.values():
                    for e, s in freeSpaces.items():
                        if r2+1 == s:
                            freeSpaces[e] = r
                            r2 = e
                            break
                if r-1 in freeSpaces:
                    freeSpaces[r2] = freeSpaces.pop(r-1)
                else:
                    freeSpaces[r2] = r
                ids[i] = (ids[i][0], start)
                changed.add(i)
                break

    id = 0
    for i in range(len(ids)):
        (l,r) = ids[i]
        for j in range(l):
            sum+= (r+j) * i
        id+=l

    return sum


if __name__ == '__main__':
    with open("../../input/day09.txt") as file:
        input = [line.rstrip() for line in file][0]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
