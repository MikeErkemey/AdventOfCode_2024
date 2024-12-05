with open("../../input/day01.txt") as file:
    input = [line.rstrip() for line in file]

left = []
right = []

for i in input:
    split = i.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

dict = dict()

for l in left:
    if l in dict:
        dict[l] += 1
    else:
        dict[l] = 1

sum = 0

for l in right:
    if l in dict:
        sum += dict[l] * l

print(sum)




