import time


def solve(input):
    input2 = [s.split("-") for s in input]
    connections = dict()

    for s in input2:
        connections.setdefault(s[0], []).append(s[1])
        connections.setdefault(s[1], []).append(s[0])

    one = set()
    for k,v in connections.items():
        for v2 in v:
            for v3 in connections[v2]:
                if v3 == k:
                    continue
                if k in connections[v3]:
                    t = (k,v2,v3)
                    t = tuple(sorted(t))
                    if t not in one:
                        one.add(t)
    one = sorted(one)

    res = 0
    for o in one:
        for c in o:
            if c[0] == 't':
                res+=1
                break
    return res
if __name__ == '__main__':
    with open("../../input/day23.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
