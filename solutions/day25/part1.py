import time


def solve(input):
    keys = []
    locks = []
    i = 0
    while i < len(input):
        if all(c == '#' for c in input[i]):
            locks.append([])
            while i < len(input) and input[i] != '':
                locks[-1].append(input[i])
                i+=1
        else:
            keys.append([])
            while i < len(input) and input[i] != '':
                keys[-1].append(input[i])
                i+=1
        i+=1

    lockPins = []
    keyShape = []

    for l in locks:
        lockPins.append([0,0,0,0,0])
        for y in l:
            if '#' in y:
                for i,e in enumerate(y):
                    if e == '#':
                        lockPins[-1][i] += 1


    for k in keys:
        keyShape.append([0,0,0,0,0])
        for y,v in enumerate(k):
            for i,e in enumerate(v):
                if e == '#' and keyShape[-1][i] == 0:
                    keyShape[-1][i] = 6 - y

    res = 0

    for l in lockPins:
        for k in keyShape:
            holds = True
            for i in range(len(l)):
                if l[i] + k[i] > 6:
                    holds = False
                    break
            if holds:
                res += 1
    return res


if __name__ == '__main__':
    with open("../../input/day25.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
