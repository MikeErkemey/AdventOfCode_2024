with open("../../input/day01.txt") as file:
    input = [line.rstrip() for line in file]

left = []
right = []

for i in input:
    split = i.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()
sum = 0

for i in range(0, len(left)):
    sum += abs(right[i] - left[i])

print(sum)
