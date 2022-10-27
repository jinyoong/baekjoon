import sys

custom_input = sys.stdin.readline

N, M = map(int, custom_input().split())
board = [list(map(int, custom_input().split())) for _ in range(N)]


def spread(lap, point, virus, wall, n, limit):
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    queue = []
    visited = set()

    for i in point:
        queue.append(virus[i] + [0])
        visited.add(tuple(virus[i]))

    idx = 0
    length = len(point)

    while idx < length:
        r, c, time = queue[idx]
        idx += 1

        if lap[r][c] == 0:
            wall -= 1

        if wall == 0:
            return time

        if time > limit:
            return 987654321

        for i in range(4):
            nr, nc = r + direction[i][0], c + direction[i][1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            if lap[nr][nc] == 1:
                continue

            if (nr, nc) in visited:
                continue

            queue.append([nr, nc, time + 1])
            visited.add((nr, nc))
            length += 1

    return 987654321


def solution(lap, n, m):
    answer = 987654321
    virus = []
    wall = 0

    for r in range(n):
        for c in range(n):

            if lap[r][c] == 2:
                virus.append([r, c])

            if lap[r][c] == 0:
                wall += 1

    if wall == 0:
        return 0

    virus_collection = []

    def collection(idx, result):

        if len(result) == m:
            virus_collection.append(result)
            return

        for i in range(idx, len(virus)):
            collection(i + 1, result + [i])

    collection(0, [])

    for ele in virus_collection:
        r = spread(lap, ele, virus, wall, n, answer)
        if r < answer:
            answer = r

    if answer == 987654321:
        return -1

    return answer


print(solution(board, N, M))
