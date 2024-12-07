import time


def solve(input):
    lookUp = {}

    rules = [[int(x) for x in (rule.split("|"))] for rule in input[:input.index("")]]
    pages = [[int(x) for x in page.split(",")] for page in input[input.index("")+1:]]
    [lookUp.setdefault(k, set()).add(v) for v, k in rules]

    return sum(
            int(sortedList[len(sortedList) // 2]) if page != sortedList else 0
            for page in pages
            for sortedList in [sorted(page, key=lambda x: len(lookUp.get(x, set()).intersection(page)))]
        )


if __name__ == '__main__':
    with open("../../input/day05.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")


