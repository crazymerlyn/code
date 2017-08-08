def isvalid(sudoku):
    for i in range(9):
        a = [x for x in sudoku[i] if x]
        if len(a) != len(set(a)):
            return False
    for j in range(9):
        a = [sudoku[i][j] for i in range(9) if sudoku[i][j]]
        if len(a) != len(set(a)):
            return False
    for i in range(9):
        a = [sudoku[i//3*3+j//3][i%3*3+j%3] for j in range(9)]
        a = [x for x in a if x]
        if len(a) != len(set(a)):
            return False
    return True

def possibs(sudoku, i, j):
    ans = set(range(1, 10))
    ans -= set(sudoku[i])
    ans -= set(sudoku[i_][j] for i_ in range(9))
    box_i = i // 3
    box_j = j // 3
    ans -= set(sudoku[box_i*3+i][box_j*3+j] for i in range(3) for j in range(3))
    return ans

def issolved(sudoku):
    return isvalid(sudoku) and all(not any(not x for x in row) for row in sudoku)

def unfilled(sudoku):
    for i in range(8, -1, -1):
        for j in range(8, -1, -1):
            if not sudoku[i][j]:
                return i, j
    return None

def solve(sudoku):
    a = unfilled(sudoku)
    if not a:
        return
    i, j = a
    for n in possibs(sudoku, i, j):
        sudoku[i][j] = n
        solve(sudoku)
        if issolved(sudoku):
            return
    sudoku[i][j] = 0

with open("./p096_sudoku.txt") as f:
    res = 0
    for i in range(50):
        name = f.readline()
        sudoku = []
        for _ in range(9):
            sudoku.append([int(x) for x in f.readline().strip()])
        solve(sudoku)
        print i
        res += int("".join(map(str, sudoku[0][:3])))
    print res

