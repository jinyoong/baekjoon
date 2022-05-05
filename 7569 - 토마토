import sys

M, N, H = map(int, input().split())

tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
queue = []
rear = 0

for h in range(H):
    for r in range(N):
        for c in range(M):

            if tomatoes[h][r][c] == 1:

                queue.append((h, r, c))
                rear += 1
                
head = 0

while head < rear:
        ch, cr, cc = queue[head]
        head += 1

        for i in range(6):
            nh, nr, nc = ch + dh[i], cr + dr[i], cc + dc[i]

            if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if tomatoes[nh][nr][nc]:
                continue

            queue.append((nh, nr, nc))
            tomatoes[nh][nr][nc] = tomatoes[ch][cr][cc] + 1
            rear += 1


def solution():
    answer = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatoes[h][r][c] == 0:
                    return -1

                answer = max(answer, tomatoes[h][r][c])
    return answer - 1

print(solution())
