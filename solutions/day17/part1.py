import sys
import time


def solve(input):
    program = [int(x) for x in input[4].split(" ")[-1].split(",")]

    # b = a%8 -> b = b^2 -> c = a//(2**b) -> b ^ c -> a // 8 -> b^7 -> print(b) -> jmp 0

    # b = (a%8^2) ^c^7
    # c = a//(2**(a%8^2))
    # a = a//8
    # print(len(outputs), len(program))

    return reverse(0,len(program)-1,program)

def reverse(a,index, program):
    arr = []
    for i in range(0,8):
        ax = a * 8 + i
        x = ((((ax%8)^2) ^ (ax//(2**((ax%8)^2))))%8) ^ 7
        if x == program[index]:
            arr.append(ax)

    if index == 0:
        return min(arr)
    if len(arr) == 0:
        return sys.maxsize

    return min([reverse(ax, index-1,program) for ax in arr])

if __name__ == '__main__':
    with open("../../input/day17.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
