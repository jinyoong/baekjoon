M, N = map(int, input().split())

banner = [list(map(int, input().split())) for _ in range(M)]
check = [[0] * N for _ in range(M)]
answer = 0
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

for i in range(M):
    for j in range(N):
        if not banner[i][j]:
            continue

        if check[i][j]:
            continue

        queue = [(i, j)]
        check[i][j] = 1
        head = 0
        rear = 1
        answer += 1

        while head < rear:
            r, c = queue[head]
            head += 1

            for k in range(8):
                nr, nc = r + dr[k], c + dc[k]

                if nr < 0 or nr >= M or nc < 0 or nc >= N:
                    continue

                if not banner[nr][nc]:
                    continue

                if check[nr][nc]:
                    continue

                queue.append((nr, nc))
                check[nr][nc] = 1
                rear += 1

print(answer)
