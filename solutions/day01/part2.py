import time


def solve(input):
    left = []
    right = []

    for i in input:
        split = i.split()
        left.append(int(split[0]))
        right.append(int(split[1]))

    dict = {}

    for l in left:
        if l in dict:
            dict[l] += 1
        else:
            dict[l] = 1

    sum = 0

    for l in right:
        if l in dict:
            sum += dict[l] * l

    return sum


if __name__ == '__main__':
    with open("../../input/day01.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")





