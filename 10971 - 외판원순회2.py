def permu(idx, N, last, value):
    global answer

    if idx == N-1:

        if not town[last][start]:
            return

        result = value + town[last][start]
        if result < answer:
            answer = result
        return

    if value >= answer:
        return

    for i in range(N):

        if used[i]:
            continue

        if not town[last][i]:
            continue

        used[i] = 1
        permu(idx + 1, N, i, value+town[last][i])
        used[i] = 0


N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]
t_lst = []
used = [0] * N
answer = 10000000

for start in range(N):
    used[start] = 1
    permu(0, N, start, 0)

print(answer)
