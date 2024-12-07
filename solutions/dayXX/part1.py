import time


def solve(input):
    return input


if __name__ == '__main__':
    with open("../../input/dayXX.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
