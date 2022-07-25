N, e, w, s, n = map(int, input().split())

d_lst = [e, w, s, n]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

field = [[0] * 40 for _ in range(40)]
answer = 0


def solution(r, c, visited, count, limit, result):
    global answer

    if count == limit:
        answer += result
        return result

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if visited[nr][nc]:
            continue

        visited[nr][nc] = 1
        solution(nr, nc, visited, count + 1, limit, result * d_lst[i] / 100)
        visited[nr][nc] = 0


field[19][19] = 1
solution(19, 19, field, 0, N, 1)
field[19][19] = 0

print(answer)
