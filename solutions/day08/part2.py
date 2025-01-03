import time

def solve(input):
    antennas  = dict()
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != '.':
                antennas[(x,y)] = input[y][x]

    chars = set(antennas.values())
    antinodes = set()
    for c in chars:
        curFreq = [k for k,v in antennas.items() if v == c]
        for i in curFreq:
            antinodes.add(i)
            for j in curFreq:
                if i == j:
                    continue
                dx = j[0]-i[0]
                dy = j[1]-i[1]
                p = (i[0] - dx, i[1] - dy)
                while 0 <= p[0] < len(input[0]) and 0 <= p[1] < len(input):
                    antinodes.add(p)
                    p = (p[0] - dx, p[1] - dy)

    return len(antinodes)

if __name__ == '__main__':
    with open("../../input/day08.txt") as file:
        input = [[c for c in line.rstrip()] for line in file]
    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
