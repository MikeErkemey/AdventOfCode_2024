import time
from functools import cache

def solve(input):
    input2 = [s.split("-") for s in input]
    connections = dict()

    for s in input2:
        connections.setdefault(s[0], set()).add(s[1])
        connections.setdefault(s[1], set()).add(s[0])

    @cache
    def getSets(p: frozenset, curSet: frozenset):
        maxParty = p
        for c in curSet:
            intersect = curSet.intersection(connections[c])
            if p.issubset(connections[c]):
                party = getSets(frozenset(p.union({c})), frozenset(intersect))
                if len(maxParty) < len(party):
                    maxParty = party
        return set(sorted(maxParty))

    partyMax = set()
    for k,v in connections.items():
        party = getSets(frozenset({k}),frozenset(v))
        if len(party) > len(partyMax):
            partyMax = party

    return ','.join(sorted(partyMax))


if __name__ == '__main__':
    with open("../../input/day23.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
