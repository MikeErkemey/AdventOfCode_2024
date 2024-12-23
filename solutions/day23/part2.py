import time

def solve(input):
    input2 = [s.split("-") for s in input]

    connections = dict()
    for s in input2:
        connections.setdefault(s[0], set()).add(s[1])
        connections.setdefault(s[1], set()).add(s[0])
    partyMax = set()
    visited = set()

    def getSets(party: frozenset, openConnections: frozenset):
        maxParty = party
        for c in openConnections:
            if c in visited:
                continue
            visited.add(c)
            if party.issubset(connections[c]):
                intersect = openConnections & connections[c]
                if len(intersect) + len(party) + 1 <= len(partyMax):
                    continue

                nParty = getSets(party | {c}, intersect)
                if len(maxParty) < len(nParty):
                    maxParty = nParty

        return maxParty

    for k,v in connections.items():
        if len(partyMax) >= len(v) or k in visited:
            continue
        visited.add(k)
        party = getSets(frozenset({k}), frozenset(v) - visited)
        if len(party) > len(partyMax):
            partyMax = party

    return ','.join(sorted(partyMax))


if __name__ == '__main__':
    with open("../../input/day23.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
