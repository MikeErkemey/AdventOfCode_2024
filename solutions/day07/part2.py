import time

def solve(input):
    values = [(int(x), [int(x) for x in y.split(" ")]) for x, y in (i.split(": ") for i in input)]
    print(sum([v[0] for v in values if helper(v[0], v[1], 1, v[1][0])]))

def helper(testValue, operations, index, curValue):
    if curValue > testValue:
        return False
    if index == len(operations):
        return curValue == testValue

    return helper(testValue, operations, index+1, curValue+operations[index]) or \
           helper(testValue, operations, index+1, curValue*operations[index]) or \
           helper(testValue, operations, index+1, int(str(curValue) + str(operations[index])))

if __name__ == '__main__':
    with open("../../input/day07.txt") as file:
        input = [line.rstrip() for line in file]\

    start = time.time()
    solve(input)
    elapsed_time = round((time.time() - start) * 1000)
    print(f"Execution Time: {elapsed_time} ms")
