import time


def solve(input):
    res = 0
    for i in input:
        secret = i
        for _ in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
        res += secret

    return res


if __name__ == '__main__':
    with open("../../input/day22.txt") as file:
        input = [int(line.rstrip()) for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
