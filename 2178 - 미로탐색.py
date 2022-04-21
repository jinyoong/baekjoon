N, M = map(int, input().split())

miro = [list(map(int, input())) for _ in range(N)]

queue = [[0, 0, 1]]
check = {(0, 0), }
head = 0
rear = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while head < rear:
    r, c, d = queue[head]
    head += 1

    if [r, c] == [N - 1, M - 1]:
        print(d)
        break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        if not miro[nr][nc]:
            continue

        if (nr, nc) in check:
            continue

        queue.append([nr, nc, d + 1])
        check.add((nr, nc))
        rear += 1
