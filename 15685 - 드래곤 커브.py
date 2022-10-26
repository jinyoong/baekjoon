import sys

custom_input = sys.stdin.readline

N = int(input())
lst = [list(map(int, custom_input().split())) for _ in range(N)]


def draw_curve(info, k):

    for _ in range(k):
        lr, lc = info[-1]
        length = len(info)

        for i in range(length - 2, -1, -1):
            r, c = info[i]
            dr, dc = lr - r, lc - c
            nr, nc = lr + -1 * dc, lc + dr

            info.append([nr, nc])

    return info


def solution(curves):
    answer = 0
    board = [[0] * 101 for _ in range(101)]
    direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    for curve in curves:
        x, y, d, g = curve

        start_curve = [[y, x], [y + direction[d][0], x + direction[d][1]]]
        draw_point = draw_curve(start_curve, g)

        for point in draw_point:
            r, c = point

            board[r][c] += 1

    for r in range(100):
        for c in range(100):

            if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
                answer += 1

    return answer


print(solution(lst))
