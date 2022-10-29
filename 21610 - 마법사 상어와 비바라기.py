import sys

custom_input = sys.stdin.readline

N, M = map(int, custom_input().split())
board = [list(map(int, custom_input().split())) for _ in range(N)]
lst = [list(map(int, custom_input().split())) for _ in range(M)]
direction = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]


def move_cloud(n, cloud, order):
    new_cloud = set()
    d, s = order

    for ele in cloud:
        r, c = ele
        nr, nc = (r + direction[d][0] * s) % n, (c + direction[d][1] * s) % n
        new_cloud.add((nr, nc))

    return new_cloud


def copy_magic(n, field, r, c):
    result = 0

    for ele in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
        nr, nc = r + ele[0], c + ele[1]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if field[nr][nc]:
            result += 1

    return result


def solution(n, field, moves):
    answer = 0
    cloud = {(-1, 0), (-1, 1), (-2, 0), (-2, 1)}

    for move in moves:

        after_move = move_cloud(n, cloud, move)
        cloud.clear()

        for ele in after_move:
            r, c = ele
            field[r][c] += 1

        for ele in after_move:
            r, c = ele
            field[r][c] += copy_magic(n, field, r, c)

        for r in range(n):
            for c in range(n):

                if (r, c) in after_move:
                    continue

                if field[r][c] >= 2:
                    cloud.add((r, c))
                    field[r][c] -= 2

    for r in range(n):
        for c in range(n):

            answer += field[r][c]

    return answer


print(solution(N, board, lst))
