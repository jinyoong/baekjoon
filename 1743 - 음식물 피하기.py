N, M, K = map(int, input().split())

trashes = [[0] * (M + 1) for _ in range(N + 1)]
trash_lst = [[] for _ in range(K)]
trash_set = set()
answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(K):
    r, c = map(int, input().split())
    trash_lst[i] = [r, c]
    trash_set.add((r, c))

for trash in trash_lst:
    result = 1
    tr, tc = trash

    if trashes[tr][tc]:
        continue

    trashes[tr][tc] = 1
    queue = [(tr, tc)]
    head = 0
    rear = 1

    while head < rear:
        r, c = queue[head]
        head += 1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr <= 0 or nr >= (N + 1) or nc <= 0 or nc >= (M + 1):
                continue

            if trashes[nr][nc]:
                continue

            if (nr, nc) not in trash_set:
                continue

            queue.append((nr, nc))
            trashes[nr][nc] = 1
            rear += 1
            result += 1

    if result > answer:
        answer = result

print(answer)
