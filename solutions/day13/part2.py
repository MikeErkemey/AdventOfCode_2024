import time
import re

def solve(input):
    index = 0
    res = 0
    while index < len(input):
        a = [int(x) for x in re.findall(r'\d+', input[index])]
        b = [int(x) for x in re.findall(r'\d+', input[index+1])]
        price = [int(x)+ 10000000000000 for x in re.findall(r'\d+', input[index+2])]
        res += winPrice(a,b,price)
        index = index+3

    return int(res)

def winPrice(a, b, price):

    top = a[1] * price[0] - a[0] * price[1]
    bottom = a[1] * b[0] - a[0] * b[1]

    if bottom == 0:
        return 0

    if top%bottom != 0:
        return 0

    bPresses = round(top/bottom)
    aPresses = round((price[0] - bPresses * b[0])/a[0])

    if price[1] == a[1] * aPresses + b[1] * bPresses:
        return aPresses * 3 + bPresses
    return 0

if __name__ == '__main__':
    with open("../../input/day13.txt") as file:
        input = [line.rstrip() for line in file if line != '\n']

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
