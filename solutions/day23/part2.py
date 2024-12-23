import time
from functools import cache

def solve(input):
    input2 = [s.split("-") for s in input]
    connections = dict()

    for s in input2:
        connections.setdefault(s[0], set()).add(s[1])
        connections.setdefault(s[1], set()).add(s[0])

    maxSize = max(len(v) for v in connections.values())

    partyMax = set()
    for k,v in connections.items():
        party = getSets({k},v,connections,maxSize)
        if len(party) > len(partyMax):
            partyMax = party

    return ','.join(sorted(partyMax))

# @cache
def getSets(p,curSet:set, connections, maxSize):
    psort = tuple(sorted(p))
    curSetSort = tuple(sorted(curSet))
    if (psort, curSetSort) in lookUp:
        return lookUp[(psort, curSetSort)]

    if len(p) >= maxSize:
        return p
    maxSet = set(sorted(p))
    for c in curSet:
        u1 = curSet.intersection(connections[c])
        u2 = p.intersection(connections[c])
        if u2 == p:
            t = getSets(p.union({c}), u1, connections, maxSize)
            if len(maxSet) < len(t):
                maxSet = t
    m = set(sorted(maxSet))
    lookUp[(psort, curSetSort)] = m
    return m



if __name__ == '__main__':
    with open("../../input/day23.txt") as file:
        input = [line.rstrip() for line in file]

    lookUp = dict()
    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
