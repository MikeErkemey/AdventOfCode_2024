import time
from functools import cache

def solve(input):
    l = input[:input.index('')]
    r = input[input.index('') + 1:]
    xe = []
    ye = []
    xb = "000000000000000000000000000000000000000000000"
    yb = "000000000000000000000000000000000000000000000"
    for j in range(45):
        inputs = dict()
        dag = dict()
        ops = dict()
        for i in range(45):
            inputs[f"x{i:02}"] = 1 if j == i else 0
            inputs[f"y{i:02}"] = int(yb[44-i])
        # print(inputs)
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

        x = sorted([(k,v) for k,v in inputs.items() if 'x' in k], key=lambda i:i[0], reverse=True)
        y = sorted([(k,v) for k,v in inputs.items() if 'y' in k], key=lambda i:i[0], reverse=True)
        z = sorted([(k,v) for k,v in inputs.items() if 'z' in k], key=lambda i:i[0], reverse=True)
        xy = int(''.join(str(s) for k,s in x), 2) + int(''.join(str(s) for k,s in y), 2)
        print(xy)
        output = bin(xy)[-len(z):]
        print(f"{xy:046b}")
        print(''.join(str(s) for k,s in z))
        if f"{xy:046b}" != ''.join(str(s) for k,s in z):
            xe.append(j)

    print(xe)

    print(int(yb, 2), int(xb,2), int(yb, 2) +  int(xb,2))
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
