import re

with open("../../input/day03.txt") as file:
    input = [line.rstrip() for line in file]


matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)',''.join(input))

sum = 0

for match in matches:
    split = re.findall(r'\d+', match)
    sum += int(split[0]) * int(split[1])

print(sum)
