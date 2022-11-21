import sys

custom_input = sys.stdin.readline

N, B = map(int, custom_input().split())
A = []
for _ in range(N):
    element = list(map(int, custom_input().split()))
    for l in range(N):
        element[l] %= 1000

    A.append(element)


def multi_matrix(matrix1, matrix2, n):
    result = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            for i in range(n):

                result[r][c] += ((matrix1[r][i] % 1000) * (matrix2[i][c] % 1000)) % 1000
                result[r][c] %= 1000

    return result


def solution(matrix, count, n):

    if count == 1:
        return matrix

    matrix_ele = solution(matrix, count // 2, n)

    if count % 2:
        return multi_matrix(multi_matrix(matrix_ele, matrix_ele, n), matrix, n)
    else:
        return multi_matrix(matrix_ele, matrix_ele, n)


answer = solution(A, B, N)
for k in range(N):
    print(*answer[k])
