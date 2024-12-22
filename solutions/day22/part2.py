import time


def solve(input):
    prices = dict()
    for i in input:
        secret = i
        prev = secret % 10
        sequences = []
        been = set()
        for j in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
            sequences.append((secret % 10) - prev)
            prev = secret % 10
            if len(sequences) >= 4:
                seq = tuple(sequences[-4:])
                if seq in been:
                    continue
                been.add(seq)
                prices[seq] = prices.setdefault(seq, 0) + prev

    return max(k for v,k in prices.items())

if __name__ == '__main__':
    with open("../../input/day22.txt") as file:
        input = [int(line.rstrip()) for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
