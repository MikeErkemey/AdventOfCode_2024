import time
import re
import sys

def solve(input):
    index = 0
    res = 0
    while index < len(input):
        a = [int(x) for x in re.findall(r'\d+', input[index])]
        b = [int(x) for x in re.findall(r'\d+', input[index+1])]
        prize = [int(x) for x in re.findall(r'\d+', input[index+2])]
        res += winPrize(a,b,prize)
        index = index+3

    return int(res)

def winPrize(a, b, price):
    aa = []
    i = 0
    while a[0]*i <= price[0] and a[1]*i <= price[1]:
        if (price[0] - a[0] * i) / b[0] == (price[1] - a[1] * i) / b[1] and (price[0] - a[0] * i) % b[0] == 0:
            aa.append(i)
        i += 1

    if len(aa) == 0:
        return 0

    return min([index * 3 + (price[0] - index * a[0]) / b[0] for index in aa])



if __name__ == '__main__':
    with open("../../input/day13.txt") as file:
        input = [line.rstrip() for line in file if line != '\n']

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
