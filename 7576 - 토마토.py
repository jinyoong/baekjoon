import sys


def bfs(queue):
    global cnt
    global rear
    front = 0

    while front < rear:
        r, c, day = queue[front]
        front += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if tomatoes[nr][nc]:
                continue

            tomatoes[nr][nc] = 1
            queue[rear] = [nr, nc, day+1]
            cnt += 1
            rear += 1

    return queue[front-1][2]


M, N = map(int, input().split())

tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0

answer = 0
queue = [[-1, -1, -1] for _ in range(M*N)]
rear = 0
for r in range(N):
    for c in range(M):
        if tomatoes[r][c] == -1:
            cnt += 1
            continue

        if tomatoes[r][c] == 1:
            cnt += 1
            queue[rear] = [r, c, 0]
            rear += 1

answer = bfs(queue)
if cnt != M*N:
    answer = -1

print(answer)
