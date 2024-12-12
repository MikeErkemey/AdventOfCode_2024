import time

def solve(input):

    arr = input

    for i in range(25):
        arr2 = []
        for stone in arr:
            if stone == 0:
                arr2.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                arr2.append(int(s[:len(s)//2]))
                arr2.append(int(s[len(s)//2:]))
            else:
                arr2.append(stone * 2024)
        arr = arr2
    return len(arr)

if __name__ == '__main__':
    with open("../../input/day11.txt") as file:
        input = [[int(c) for c in line.rstrip().split(" ")] for line in file][0]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
