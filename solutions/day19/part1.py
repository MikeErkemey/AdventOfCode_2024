import time
from functools import cache


def solve(input):
    patterns = tuple(input[:input.index('')][0].split(", "))
    towels = input[input.index('')+1:]
    return sum(1 if isPossible(t,0,patterns) else 0 for t in towels)


@cache
def isPossible(towel, iTowel, patterns):
    if iTowel == len(towel):
        return True
    for p in patterns:
        l = len(p)
        if l + iTowel > len(towel):
            continue

        if p == towel[iTowel: iTowel + l]:
            if isPossible(towel, iTowel + l, patterns):
                return True
    return False

if __name__ == '__main__':
    with open("../../input/day19.txt") as file:
        input = [line.rstrip() for line in file]

    patterns = input[:input.index('')][0].split(", ")
    towels = input[input.index('')+1:]
    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
