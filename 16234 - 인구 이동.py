def moving():
    answer = 0

    while True:
        answer += 1
        check = set()
        is_change = False
        for r in range(N):
            for c in range(N):
                if (r, c) in check:
                    continue

                check.add((r, c))
                queue = [[r, c]]
                people = countries[r][c]
                head = 0
                rear = 1

                while head < rear:
                    r, c = queue[head]
                    head += 1
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]

                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue

                        if (nr, nc) in check:
                            continue

                        if L <= abs(countries[r][c] - countries[nr][nc]) <= R:
                            check.add((nr, nc))
                            people += countries[nr][nc]
                            queue.append([nr, nc])
                            rear += 1
                            is_change = True

                if is_change:
                    for ele in queue:
                        tr, tc = ele
                        countries[tr][tc] = people // len(queue)

        if not is_change:
            return answer - 1


N, L, R = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
countries = []
for _ in range(N):
    countries.append(list(map(int, input().split())))

print(moving())
