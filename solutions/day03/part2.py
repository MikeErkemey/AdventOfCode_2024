import re

with open("../../input/day03.txt") as file:
    input = [line.rstrip() for line in file]


matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)",''.join(input))

sum = 0
do = True

for match in matches:
    if "do" in match:
        do = "do()" == match
        continue
    if do:
        split = re.findall(r'\d+', match)
        sum += int(split[0]) * int(split[1])

print(sum)