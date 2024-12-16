import time
from collections import deque


def solve(input):
    m = input[:input.index('')]
    instructions = input[input.index('') + 1:]

    dirs = {'<' : (-1,0), 'v' : (0,1), '^' : (0,-1),'>' : (1,0)}
    box = {'[' : 1, ']' : -1}


    matrix = []
    points = dict()
    x = 0
    y = 0
    for i in range(len(m)):
        matrix.append([])
        for j in range(len(m[i])):
            if m[i][j] == 'O':
                matrix[i].extend(["[", "]"])
            elif m[i][j] == '@':
                matrix[i].extend(["@", "."])
            else:
                matrix[i].extend([m[i][j], m[i][j]])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '.':
                points[(j,i)] = matrix[i][j]
                if matrix[i][j] == '@':
                    y = i
                    x = j

    for dir in ''.join(instructions):
        if dir == '<' or dir == '>':
            (dx,dy) = dirs[dir]
            x2 = x + dx
            y2 = y + dy
            while (x2,y2) in points and points[(x2,y2)] != '#':
                x2 = x2 + dx
                y2 = y2 + dy

            if (x2,y2) not in points:
                while True:
                    points[(x2,y2)] = points[(x2 - dx, y2 - dy)]
                    x2 = x2 - dx
                    y2 = y2 - dy
                    if x2 == x and y2 == y:
                        points.pop((x,y))
                        x += dx
                        y += dy
                        break
        else:
            movable = True
            (dx,dy) = dirs[dir]
            x2 = x + dx
            y2 = y + dy
            move = set()
            q = deque()
            if (x2,y2) in points and (points[(x2,y2)] == '[' or points[(x2,y2)] == ']'):
                q.append((x2,y2))
                q.append((x2 + box[points[(x2,y2)]],y2))


            while len(q) != 0:
                c = q.popleft()
                if c in move:
                    continue
                move.add(c)
                c2 = (c[0] + dx, c[1] + dy)
                if c2 in points:
                    if points[c2] == '#':
                        movable = False
                        break
                    if points[c2] == '[' or points[c2] == ']':
                        q.append(c2)
                        q.append((c2[0] + box[points[c2]],c2[1]))
            if not movable:
                continue

            for p in sorted(move, key= lambda r : r[1] * -dy):
                points[(p[0]+dx, p[1]+dy)] = points[p]
                points.pop(p)


            if (x2,y2) not in points:
                while True:
                    points[(x2,y2)] = points[(x2 - dx, y2 - dy)]
                    x2 = x2 - dx
                    y2 = y2 - dy
                    if x2 == x and y2 == y:
                        points.pop((x,y))
                        x += dx
                        y += dy
                        break

    return sum([p[0] + p[1] * 100 for p in points if points[p] == '['])

if __name__ == '__main__':
    with open("../../input/day15.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
