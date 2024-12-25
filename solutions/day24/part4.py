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

    # z08, vvr, kwv
    # z16, kbg, mcc
    # z28, tfb, gws
    # z39, mqh, jds
    zValue = 'z08'
    xv = 'vvr'
    temp = dag[zValue]
    dag[zValue] = dag[xv]
    dag[xv] = temp
    temp = ops[zValue]
    ops[zValue] = ops[xv]
    ops[xv] = temp
    # rnq, bkr
    zValue = 'rnq'
    xv = 'bkr'
    temp = dag[zValue]
    dag[zValue] = dag[xv]
    dag[xv] = temp
    temp = ops[zValue]
    ops[zValue] = ops[xv]
    ops[xv] = temp

    zValue = 'z28'
    xv = 'tfb'
    temp = dag[zValue]
    dag[zValue] = dag[xv]
    dag[xv] = temp
    temp = ops[zValue]
    ops[zValue] = ops[xv]
    ops[xv] = temp

    zValue = 'z39'
    xv = 'mqh'
    temp = dag[zValue]
    dag[zValue] = dag[xv]
    dag[xv] = temp
    temp = ops[zValue]
    ops[zValue] = ops[xv]
    ops[xv] = temp

    for k,v in dag.items():
        findPath(k,v)

    x = sorted([(k,v) for k,v in inputs.items() if 'x' in k], key=lambda i:i[0], reverse=True)
    y = sorted([(k,v) for k,v in inputs.items() if 'y' in k], key=lambda i:i[0], reverse=True)
    z = sorted([(k,v) for k,v in inputs.items() if 'z' in k], key=lambda i:i[0], reverse=True)
    print(x,z)
    xy = int(''.join(str(s) for k,s in x), 2) + int(''.join(str(s) for k,s in y), 2)

    output = bin(xy)[-len(z):]
    print(output)
    print(''.join(str(s) for k,s in z))
    print(xy)
    print( int(''.join(str(s) for k,s in z), 2))


    return ','.join(sorted(['z08','bkr','z28', 'z39','vvr', 'rnq', 'tfb', 'mqh']))

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
