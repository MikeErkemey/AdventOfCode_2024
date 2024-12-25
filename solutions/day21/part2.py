import time
import sys
from functools import cache

def solve(input):
    numPad = [['7','8','9'],
             ['4','5','6'],
             ['1','2','3'],
             [None,'0', 'A']]
    keyPad = [[None, '^', 'A'],
              ['<','v','>']]

    np = dict((numPad[i][j], (j, i)) for i in range(len(numPad)) for j in range(len(numPad[0])) if numPad[i][j] != None)
    kp = dict((keyPad[i][j], (j, i)) for i in range(len(keyPad)) for j in range(len(keyPad[0])) if keyPad[i][j] != None)
    dirs = {'<': (-1, 0), 'v': (0, 1), '^': (0, -1), '>': (1, 0)}

    @cache
    def findMin(s, e, m, level, cost, fs, isNP):
        pad = np if isNP else kp

        if s not in pad.values():
            return sys.maxsize

        if level == 0:
            return 1

        if s == e:
            return cost + findMin(kp.get(m), kp.get('A'), 'A', level-1, 0, frozenset({}), False)

        sx, sy = s
        test = []

        for d, k in dirs.items():
            dx, dy = k
            ns = (sx + dx, sy + dy)
            if ns in fs:
                continue
            nfs = fs | {s}
            t2 = findMin(kp.get(m), kp.get(d), 'A', level-1, 0, frozenset({}), False)
            t = findMin(ns, e, d, level, 0, nfs, isNP)
            test.append(t + t2)
            if ns == e:
                break
        if len(test) == 0:
            return sys.maxsize

        return min(test)

    res = 0
    for i in input:
        prev = 'A'
        temp2 = 0
        for j in i:
            temp = findMin(np.get(prev), np.get(j), "A",26, 0, frozenset({}), True)
            temp2 += temp
            prev = j
        res += temp2 * int(i[:-1])

    return res

if __name__ == '__main__':
    with open("../../input/day21.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")