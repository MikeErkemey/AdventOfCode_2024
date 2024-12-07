import time


def solve(input):
    sum = 0

    for i in range(0,len(input)):
        for j in range(0,len(input[i])):
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= j+y*3 < len(input) and 0 <= i+x*3 < len(input) and not(x == 0 and y == 0):
                        if input[i+x*0][j+y*0] + input[i+x*1][j+y*1] + input[i+x*2][j+y*2] + input[i+x*3][j+y*3] == "XMAS":
                            sum += 1
    return sum


if __name__ == '__main__':
    with open("../../input/day04.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")

