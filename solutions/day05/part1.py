import time


def solve(input):
    dict = {}
    index = -1
    for i in input:
        if i == "":
            index = input.index(i) + 1
            break

        split = i.split("|")
        l = int(split[0])
        r = int(split[1])

        if r in dict:
            dict[r].add(l)
        else:
            dict[r] = {l}
    sum = 0

    for i in range(index, len(input)):
        seen = set()
        page = [int(x) for x in input[i].split(",")]
        valid = True

        for p in page:
            if p in seen:
                valid = False
                break
            if p in dict:
                seen = seen.union(dict.get(p))

        if valid:
            sum += page[len(page) // 2]

    return sum


if __name__ == '__main__':
    with open("../../input/day05.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")



