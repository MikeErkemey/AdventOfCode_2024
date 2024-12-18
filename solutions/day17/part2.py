import time


def solve(input):
    a = int(input[0].split(" ")[-1])
    b = int(input[1].split(" ")[-1])
    c = int(input[2].split(" ")[-1])
    program = [int(x) for x in input[4].split(" ")[-1].split(",")]
    o = [0,1,2,3,a,b,c]
    outputs = []
    i = 0

    while i+1 < len(program):
        opcode = program[i]
        operand = program[i+1]
        if opcode == 0:
            v = o[operand]
            o[4] = o[4]//(2**v)
        if opcode == 1:
            o[5] = o[5] ^ operand
        if opcode == 2:
            v = o[operand]
            o[5] = v % 8
        if opcode == 3:
            if o[4] != 0:
                i = operand
                continue
        if opcode == 4:
            o[5] = o[5] ^ o[6]
        if opcode == 5:
            v = o[operand]
            outputs.append(v%8)
        if opcode == 7:
            v = o[operand]
            o[6] = o[4]//(2**v)
        i += 2

    return ','.join([str(x) for x in outputs])


if __name__ == '__main__':
    with open("../../input/day17.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
