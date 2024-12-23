import time
from functools import cache

def solve(input):
    input2 = [s.split("-") for s in input]
    connections = dict()

    for s in input2:
        connections.setdefault(s[0], set()).add(s[1])
        connections.setdefault(s[1], set()).add(s[0])

    partyMax = set()

    @cache
    def getSets(p: frozenset, curSet: frozenset):
        maxSet = set(sorted(p))
        for c in curSet:
            i1 = curSet.intersection(connections[c])
            i2 = p.intersection(connections[c])
            if i2 == p:
                t = getSets(frozenset(p.union({c})), frozenset(i1))
                if len(maxSet) < len(t):
                    maxSet = t
        m = set(sorted(maxSet))
        return m

    for k,v in connections.items():
        party = getSets(frozenset({k}),frozenset(v))
        if len(party) > len(partyMax):
            partyMax = party

    return ','.join(sorted(partyMax))

# @cache



if __name__ == '__main__':
    with open("../../input/day23.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
