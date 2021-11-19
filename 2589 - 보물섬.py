mr, mc = map(int, input().split())
treasure = list(list(input()) for _ in range(mr))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(treasure):
    answer = 0
    queue = [(0, 0, 0) for _ in range(mr * mc)]
    for i in range(mr):
        for j in range(mc):
            if treasure[i][j] == 'W':
                continue

            queue[0] = (i, j, 0)
            check = {(i, j)}
            head = 0
            rear = 1

            while head < rear:
                r, c, time = queue[head]
                time += 1
                head += 1

                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if nr < 0 or nr >= mr or nc < 0 or nc >= mc:
                        continue

                    if treasure[nr][nc] == 'W':
                        continue

                    if (nr, nc) in check:
                        continue

                    queue[rear] = (nr, nc, time)
                    check.add((nr, nc))
                    rear += 1

            if answer < queue[rear-1][2]:
                answer = queue[rear-1][2]

    return answer


print(solution(treasure))