with open("../../input/day04.txt") as file:
    input = [line.rstrip() for line in file]

sum = 0

for i in range(0,len(input) - 2):
    for j in range(0,len(input[i]) - 2):
        if input[i+1][j+1] == 'A':
            if {input[i][j],input[i+2][j+2]} == {'M','S'} and {input[i+2][j],input[i][j+2]} == {'M','S'}:
                sum += 1
print(sum)

