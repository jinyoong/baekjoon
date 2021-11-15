C, R = map(int, input().split())
K = int(input())


def solution(C, R, K):
    if K > C * R:
        return (0,)

    answer = [(0, 0)] * (C * R + 1)
    seat = [[0] * C for _ in range(R)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    idx = 1
    cr = R
    cc = 0
    k = 0

    while idx <= C * R:
        nr = cr + dr[k]
        nc = cc + dc[k]

        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            k = (k + 1) % 4
            continue

        if seat[nr][nc]:
            k = (k + 1) % 4
            continue

        seat[nr][nc] = idx
        answer[idx] = (nc + 1, R - nr)
        idx += 1
        cr, cc = nr, nc

    return answer[K]


print(*solution(C, R, K))
