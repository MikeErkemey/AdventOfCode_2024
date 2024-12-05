with open("../../input/day05.txt") as file:
    input = [line.rstrip() for line in file]

dict = {}
index = -1
for i in input:
    if i == "":
        index = input.index(i) + 1
        break

    split = i.split("|")
    l = int(split[0])
    r = int(split[1])

    if r in dict:
        dict[r].add(l)
    else:
        dict[r] = {l}
sum = 0

print(dict)

for i in range(index, len(input)):
    seen = set()
    page = [int(x) for x in input[i].split(",")]
    valid = True

    for p in page:
        if p in seen:
            valid = False
            break
        if p in dict:
            seen = seen.union(dict.get(p))

    if valid:
        sum += page[len(page) // 2]

print(sum)




