import sys

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0

N, M = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def tetromino(sr, sc, count, result, check, back_count):
    global answer

    if count == 4:
        if result > answer:
            answer = result
        return

    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        if (nr, nc) in check and back_count:
            continue

        if (nr, nc) in check and not back_count:
            tetromino(nr, nc, count, result, check, 1)
            continue

        tetromino(nr, nc, count + 1, result + numbers[nr][nc], check + [(nr, nc)], back_count)


for r in range(N):
    for c in range(M):
        tetromino(r, c, 1, numbers[r][c], [(r, c)], 0)

print(answer)
