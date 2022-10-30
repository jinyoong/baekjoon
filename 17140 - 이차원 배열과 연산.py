import sys

custom_input = sys.stdin.readline

R, C, K = map(int, custom_input().split())
A = [[0] * 100 for _ in range(100)]
width = 0
height = 3
for i in range(3):
    numbers = list(map(int, custom_input().split()))
    if len(numbers) > width:
        width = len(numbers)

    for j in range(len(numbers)):
        A[i][j] = numbers[j]


def solution(n, m, board, tr, tc, tk):
    answer = 0

    while True:

        if answer > 100:
            return -1

        if board[tr][tc] == tk:
            return answer

        answer += 1
        new_n = n
        new_m = m

        if n >= m:
            for r in range(n):
                number_dict = dict()

                for c in range(m):
                    number = board[r][c]
                    board[r][c] = 0
                    number_dict[number] = number_dict.get(number, 0) + 1

                temp_lst = []
                for key, value in number_dict.items():
                    if key == 0:
                        continue
                    temp_lst.append((key, value))
                temp_lst.sort(key=lambda x: (x[1], x[0]))

                if new_m < len(temp_lst) * 2:
                    new_m = len(temp_lst) * 2

                idx = 0
                for ele in temp_lst:
                    number, count = ele
                    board[r][idx] = number
                    board[r][idx + 1] = count
                    idx += 2

        else:
            for c in range(m):
                number_dict = dict()
                for r in range(n):
                    number = board[r][c]
                    board[r][c] = 0
                    number_dict[number] = number_dict.get(number, 0) + 1

                temp_lst = []
                for key, value in number_dict.items():
                    if key == 0:
                        continue
                    temp_lst.append((key, value))
                temp_lst.sort(key=lambda x: (x[1], x[0]))

                if new_n < len(temp_lst) * 2:
                    new_n = len(temp_lst) * 2

                idx = 0
                for ele in temp_lst:
                    number, count = ele
                    board[idx][c] = number
                    board[idx + 1][c] = count
                    idx += 2

        n, m = new_n, new_m


print(solution(height, width, A, R - 1, C - 1, K))
