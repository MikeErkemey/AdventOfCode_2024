import time
from functools import cache

def solve(input):
    l = input[:input.index('')]
    r = input[input.index('') + 1:]
    inputs = dict()
    dag = dict()
    ops = dict()

    for i in l:
        split = i.split(": ")
        inputs[split[0]] = int(split[1])

    for i in r:
        split = i.split(" ")
        dag[split[4]] = (split[0],split[2])
        ops[split[4]] = split[1]

    def findPath(k, v):
        (x,y) = v
        if k in inputs:
            return
        if x in inputs and y in inputs:
            inputs[k] = value(inputs[x],inputs[y], ops[k])
            return
        findPath(x, dag[x])
        findPath(y, dag[y])
        inputs[k] = value(inputs[x],inputs[y], ops[k])
        return

    for k,v in dag.items():
        findPath(k,v)

    z = sorted([(k,v) for k,v in inputs.items() if 'z' in k], key=lambda i:i[0], reverse=True)

    return int(''.join(str(s) for k,s in z), 2)

def value(x,y,op):
    if "XOR" in op:
        return x ^ y
    elif "OR" in op:
        return x | y
    else:
        return x & y


if __name__ == '__main__':
    with open("../../input/day24.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
