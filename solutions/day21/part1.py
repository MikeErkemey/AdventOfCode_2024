import time


def solve(input):
    numPad = [['7','8','9'],
             ['4','5','6'],
             ['1','2','3'],
             [None,'0', 'A']]
    keyPad = [[None, '^', 'A'],
              ['<','v','>']]

    np = dict((numPad[i][j], (j, i)) for i in range(len(numPad)) for j in range(len(numPad[0])))
    kp = dict((keyPad[i][j], (j, i)) for i in range(len(keyPad)) for j in range(len(keyPad[0])))
    res = 0
    for i in input:
        solutions = control(i,np,np.get('A'), 0)
        for _ in range(2):

            l = min(len(s) for s in solutions)
            s1 = []
            for s in solutions:
                if s != '':
                    for x in control(s, kp,kp.get('A'),0):
                        s1.append(x)
            solutions = s1
        res += int(i[:-1]) * min(len(s) for s in solutions)

    return res

def control(code, pad, cp, index):
    if index >= len(code):
        return set()
    arrX = []
    arrY = []
    cx,cy = cp
    px,py = pad.get(None)
    c = code[index]
    nx,ny = pad.get(c)
    dx,dy = nx - cx, ny - cy
    for _ in range(abs(dy)):
        if dy < 0:
            arrY.append('^')
        else:
            arrY.append('v')
    for _ in range(abs(dx)):
        if dx < 0:
            arrY.append('<')
        else:
            arrY.append('>')
    for _ in range(abs(dx)):
        if dx < 0:
            arrX.append('<')
        else:
            arrX.append('>')
    for _ in range(abs(dy)):
        if dy < 0:
            arrX.append('^')
        else:
            arrX.append('v')
    np = nx,ny
    arr = set()
    if not(nx == 0 and cy == py):
        arrX.append('A')
        arr.add(''.join(arrX))
    if not(cx == 0 and ny == py):
        arrY.append('A')
        arr.add(''.join(arrY))

    res = set()
    for con in control(code, pad, np, index+1):
        for a in arr:
            res.add(a + con)

    if len(code)-1 == index:
        return arr
    return res


if __name__ == '__main__':
    with open("../../input/day21.txt") as file:
        input = [line.rstrip() for line in file]

    start = time.time()
    print(solve(input))
    print(f"Execution Time: {round((time.time() - start) * 1000)} ms")
