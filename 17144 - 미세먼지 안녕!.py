import sys

custom_input = sys.stdin.readline

R, C, T = map(int, custom_input().split())
board = [[] for _ in range(R)]
top = bottom = 0
for i in range(R):
    element = list(map(int, custom_input().split()))

    if element[0] == -1 and top == 0:
        top = i
        bottom = i + 1

    board[i] = element


def air_cleaner(room, n, m):
    direction = [[[1, 0], [0, 1], [-1, 0], [0, -1]], [[-1, 0], [0, 1], [1, 0], [0, -1]]]
    tsr, tsc = top - 1, 0
    bsr, bsc = bottom + 1, 0

    d_idx = 0
    while True:

        nr, nc = tsr + direction[1][d_idx][0], tsc + direction[1][d_idx][1]

        if nr < 0 or nr > top or nc < 0 or nc >= m:
            d_idx += 1
            nr = tsr + direction[1][d_idx][0]
            nc = tsc + direction[1][d_idx][1]

        if [nr, nc] == [top, 0]:
            room[tsr][tsc] = 0
            break

        room[tsr][tsc] = room[nr][nc]
        tsr, tsc = nr, nc

    d_idx = 0
    while True:

        nr, nc = bsr + direction[0][d_idx][0], bsc + direction[0][d_idx][1]

        if nr < bottom or nr >= n or nc < 0 or nc >= m:
            d_idx += 1
            nr = bsr + direction[0][d_idx][0]
            nc = bsc + direction[0][d_idx][1]

        if [nr, nc] == [bottom, 0]:
            room[bsr][bsc] = 0
            break

        room[bsr][bsc] = room[nr][nc]
        bsr, bsc = nr, nc

    return room


def solution(room, t, n, m):
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    answer = 2

    for _ in range(t):
        new_room = [[0] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):

                if room[r][c] == 0:
                    continue

                if room[r][c] == -1:
                    new_room[r][c] = -1
                    continue

                start_amount = room[r][c]
                remain_amount = room[r][c]
                for k in range(4):
                    adj_r, adj_c = r + direction[k][0], c + direction[k][1]

                    if adj_r < 0 or adj_r >= n or adj_c < 0 or adj_c >= m:
                        continue

                    if [adj_r, adj_c] == [top, 0] or [adj_r, adj_c] == [bottom, 0]:
                        continue

                    new_room[adj_r][adj_c] += start_amount // 5
                    remain_amount -= start_amount // 5

                new_room[r][c] += remain_amount

        new_room[top - 1][0] = 0
        new_room[bottom + 1][0] = 0
        room = air_cleaner(new_room, n, m)

    for r in range(n):
        for c in range(m):
            if room[r][c]:
                answer += room[r][c]

    return answer


print(solution(board, T, R, C))
