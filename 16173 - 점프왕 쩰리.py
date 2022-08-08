N = int(input())
jump_map = [list(map(int, input().split())) for _ in range(N)]
direction = [[0, 1], [1, 0]]


def solution():
    queue = [(0, 0)]
    idx = 0
    length = 1
    visited = [[0] * N for _ in range(N)]
    isClear = False

    while idx < length:
        r, c = queue[idx]
        visited[r][c] = 1
        step = jump_map[r][c]
        idx += 1

        if r == N - 1 and c == N - 1:
            isClear = True
            break

        for i in range(2):
            nr, nc = r + direction[i][0] * step, c + direction[i][1] * step

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if visited[nr][nc]:
                continue

            queue.append((nr, nc))
            length += 1

    if isClear:
        return "HaruHaru"
    else:
        return "Hing"


print(solution())
