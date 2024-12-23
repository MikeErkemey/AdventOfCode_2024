import time
from functools import cache

def solve(input):
    input2 = [s.split("-") for s in input]
    connections = dict()

    for s in input2:
        connections.setdefault(s[0], set()).add(s[1])
        connections.setdefault(s[1], set()).add(s[0])

    @cache
    def getSets(party: frozenset, openConnections: frozenset):
        maxParty = party
        for c in openConnections:
            intersect = openConnections.intersection(connections[c])
            if party.issubset(connections[c]):
                nParty = getSets(frozenset(party.union({c})), frozenset(intersect))
                if len(maxParty) < len(nParty):
                    maxParty = nParty
        return set(sorted(maxParty))

    partyMax = set()
    for k,v in connections.items():
        if len(partyMax) >= len(v):
            continue
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
