import time
import re
from functools import cache
import sys
# sys.setrecursionlimit(150000)

def solve(input):
    l = input[:input.index('')]
    r = input[input.index('') + 1:]
    inputs = dict()
    dag = dict()
    ops = dict()
    counts = dict()
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

    def makeTrees(k, v, z):
        if k not in counts:
            counts[k] = set()
        counts[k].add(z)
        (x,y) = v
        if x in inputs:
            print("(" + x, end='')
        else:
            print("(" + x+":", end='')
            makeTrees(x, dag[x],z)
        print(" " + ops[k], end=' ')
        if y in inputs:
            print(y+")", end='')
        else:
            print(y + ":", end='')
            makeTrees(y, dag[y],z)
            print(")", end='')
        return


    def makeTrees2(k, v, arr):
        (x,y) = v
        if x in inputs:
            arr.append("(")
            arr.append(x)
        else:
            arr.append("(")
            makeTrees2(x, dag[x],arr)

        arr.append(" " + ops[k] + " ")
        if y in inputs:
            arr.append(y+")")
        else:
            makeTrees2(y, dag[y], arr)
            arr.append(")")
        return
    ['z08', 'z16', 'z28', 'z39']
    zese  = {'z01','z03','z02', 'z08', 'z16', 'z28', 'z39', 'z44'}
    for k,v in dag.items():
        if k in zese:
            print(k, end=': ')
            makeTrees(k,v, 'z08')
            print()
    trees = dict()
    for k,v in dag.items():
        arr = []
        # print(k, end=': ')
        makeTrees2(k,v, arr)
        trees[k] = ''.join(arr)

    zValue = 16
    print()
    for k in counts.keys():
        tree = trees[k]
        if any(int(x) > zValue for x in re.findall(r'\d+', tree)):
            continue
        if f'{zValue:02}' in tree and  len(trees[k]) > 13:

            arr = []
            arr2 = []
            temp = dag[k]
            dag[k] = dag[f'z{zValue:02}']
            dag[f'z{zValue:02}'] = temp
            makeTrees2(f'z{zValue:02}', dag[f'z{zValue:02}'], arr)
            trees[k] = ''.join(arr)
            temp = dag[k]
            dag[k] = dag[f'z{zValue:02}']
            dag[f'z{zValue:02}'] = temp
            makeTrees2(k, dag[k], arr2)
            print(f'z{zValue:02}', ''.join(arr))
            print(k, ''.join(arr2))



    # for i in counts.keys():
    #     if 'z' not in i and counts[i] != 'z28':
    #         print(counts[i])
    #         temp = dag[i]
    #         dag[i] = dag['z28']
    #         dag['z28'] = temp
    #         makeTrees2('z28', dag['z28'])

    # print(counts)
    #
    # print(len(counts.keys()))
    # for k,v in dag.items():
    #     findPath(k,v)

    # x = sorted([(k,v) for k,v in inputs.items() if 'x' in k], key=lambda i:i[0], reverse=True)
    # y = sorted([(k,v) for k,v in inputs.items() if 'y' in k], key=lambda i:i[0], reverse=True)
    # z = sorted([(k,v) for k,v in inputs.items() if 'z' in k], key=lambda i:i[0], reverse=True)
    # xy = int(''.join(str(s) for k,s in x), 2) + int(''.join(str(s) for k,s in y), 2)
    #
    # output = bin(xy)[-len(z):]
    # print(output)
    # print(''.join(str(s) for k,s in z))
    # print(xy)

    return 0
# z08, vvr, kwv
# z16, kbg, mcc
# z28, tfb, gws
# z39, mqh, jds

# def makeTrees(k, v):
#     (x,y) = v
#     if x in inputs:
#         print("(" + x, end='')
#     else:
#         print("(", end='')
#         makeTrees(x, dag[x])
#     print(" " + ops[k], end=' ')
#     if y in inputs:
#         print(y+")", end='')
#     else:
#         makeTrees(y, dag[y])
#         print(")", end='')
#     return
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
