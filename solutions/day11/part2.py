import time

def solve(input):
    lookUp = dict() #lookUp is not needed
    stones = dict()
    for i in input:
        stones[i] = 1

    for i in range(75):
        newStones = dict()
        for stone, x in stones.items():
            if stone in lookUp:
                for s in lookUp[stone]:
                    addStone(newStones,s, x)
            elif stone == 0:
                lookUp[stone] = {1}
                addStone(newStones,1, x)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                l = int(s[:len(s)//2])
                r =int(s[len(s)//2:])
                lookUp[stone] = (l, r)
                addStone(newStones,l, x)
                addStone(newStones,r, x)
            else:
                lookUp[stone] = {stone * 2024}
                addStone(newStones,stone * 2024, x)
        stones = newStones

    return sum(stones.values())

def addStone(newStones, stone, x):
    if stone in newStones:
        newStones[stone] = newStones[stone] + x
    else:
        newStones[stone] = x

if __name__ == '__main__':
    with open("../../input/day11.txt") as file:
        input = [[int(c) for c in line.rstrip().split(" ")] for line in file][0]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
