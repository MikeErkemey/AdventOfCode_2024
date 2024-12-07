import time


def solve(input):
    matrix = [list(map(int, x)) for x in (i.split() for i in input)]

    counter = 0
    for level in matrix:
        higher = None
        holds = True
        for j in range(0, len(level)-1):
            if(higher == None):
                if level[j] < level[j+1]:
                    higher = False
                else:
                    higher = True
            if higher and level[j] <= level[j+1]:
                holds = False
                break
            if not higher and level[j] >= level[j+1]:
                holds = False
                break
            if abs(level[j] - level[j+1]) > 3:
                holds = False
                break
        if holds:
            counter += 1

    return counter


if __name__ == '__main__':
    with open("../../input/day02.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")





