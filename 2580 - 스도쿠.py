import sys

custom_input = sys.stdin.readline

board = []
lst = []
count = 0
is_print = False

for r in range(9):
    temp = list(map(int, custom_input().split()))
    board.append(temp)
    for c in range(9):
        if temp[c] != 0:
            continue

        lst.append([r, c])
        count += 1


def solution(sudoku, idx):
    global is_print

    if is_print:
        return

    if idx == count:
        for result_row in range(9):
            print(*sudoku[result_row])
        exit(0)

    temp_sudoku = [element[:] for element in sudoku]
    tr, tc = lst[idx]
    for i in range(1, 10):

        if garo(temp_sudoku, tr, i) and sero(temp_sudoku, tc, i) and rect(temp_sudoku, (tr // 3) * 3, (tc // 3) * 3, i):
            temp_sudoku[tr][tc] = i
            solution(temp_sudoku, idx + 1)
            temp_sudoku[tr][tc] = 0


def rect(sudoku, start_row, start_col, target):
    for sr in range(start_row, start_row + 3):
        for sc in range(start_col, start_col + 3):

            ele = sudoku[sr][sc]
            if ele == target:
                return False

    return True


def garo(sudoku, garo_idx, target):
    for ele in sudoku[garo_idx]:

        if ele == target:
            return False

    return True


def sero(sudoku, sero_idx, target):
    for ss in range(9):

        ele = sudoku[ss][sero_idx]
        if ele == target:
            return False

    return True


solution(board, 0)
