import time
from queue import PriorityQueue
import copy
def solve(input):
    pq = PriorityQueue()
    s = (1, len(input)-2)
    e = (len(input[1])-2, 1)

    pq.put((0,s,(1,0),set()))
    visited = set()
    v = s
    c = 0
    dirs = {(-1, 0), (0, 1), (0, -1), (1, 0)}
    n = set()
    while v != e:
        (c,v,f,n) = pq.get()
        visited.add((v,f))
        visited.add((v,(-f[0],-f[1])))

        for d in dirs:
            p = (v[0] + d[0], v[1] + d[1])
            if (p,d) in visited:
                continue
            if input[p[1]][p[0]] != '#':
                nd = (abs(d[0] - f[0]),abs(d[1] - f[1]))
                sets = copy.deepcopy(n)
                sets.add(v)
                if sum(nd) == 0:
                    pq.put((c + 1, p, d,sets))
                elif 0 not in nd:
                    pq.put((c + 1001, p, d,sets))

    while True:
        (c2,v2,f2,n2) = pq.get()
        if v2 == v and c2 ==c:
            n = n.union(n2)
        else:
            break

    return len(n) + 1


if __name__ == '__main__':
    with open("../../input/day16.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
