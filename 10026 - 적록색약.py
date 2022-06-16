N = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def count_area_blind(start):
    queue = [start]
    head = 0
    rear = 1

    while head < rear:
        cr, cc = queue[head]
        start_color = painting[cr][cc]
        blind[cr][cc] = True
        head += 1

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if blind[nr][nc]:
                continue

            if painting[nr][nc] != start_color:
                continue

            queue.append((nr, nc))
            rear += 1


def count_area_non_blind(start):
    queue = [start]
    head = 0
    rear = 1

    while head < rear:
        cr, cc = queue[head]
        start_color = painting[cr][cc]
        non_blind[cr][cc] = True
        head += 1

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if non_blind[nr][nc]:
                continue

            if start_color == "B" and painting[nr][nc] != "B":
                continue

            if start_color in {"R", "G"} and painting[nr][nc] not in {"R", "G"}:
                continue

            queue.append((nr, nc))
            rear += 1


painting = [list(input()) for _ in range(N)]
blind = [[False] * N for _ in range(N)]
non_blind = [[False] * N for _ in range(N)]
blind_answer = 0
non_blind_answer = 0

for r in range(N):
    for c in range(N):
        if not blind[r][c]:
            count_area_blind((r, c))
            blind_answer += 1

        if not non_blind[r][c]:
            count_area_non_blind((r, c))
            non_blind_answer += 1

print(blind_answer, non_blind_answer)
