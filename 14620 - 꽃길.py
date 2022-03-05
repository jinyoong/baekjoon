N = int(input())

flower_bed = [[] for _ in range(N)]

for i in range(N):
    flower_bed[i] = list(map(int, input().split()))

costs = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(1, N-1):
    for c in range(1, N-1):
        costs[r][c] = flower_bed[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            costs[r][c] += flower_bed[nr][nc]

answer = 3000


def solution(cnt, result, check):
    global answer

    if cnt == 3:
        if answer > result:
            answer = result
        return

    for r in range(1, N-1):
        for c in range(1, N-1):

            continue_true = False
            for ele in check:
                er, ec = ele
                if abs(er-r) + abs(ec-c) <= 2:
                    continue_true = True
                    break

            if continue_true:
                continue

            solution(cnt+1, result+costs[r][c], check+[[r, c]])


for r in range(1, N-1):
    for c in range(1, N-1):
        solution(1, costs[r][c], [[r, c]])

print(answer)
