N, K = map(int, input().split())

lst = [i+1 for i in range(N)]
answer = [0] * N
ans_idx = 0
idx = -1

while lst != [0] * N:
    for _ in range(K):
        idx = (idx + 1) % N
        while not lst[idx]:
            idx = (idx + 1) % N

    answer[ans_idx] = lst[idx]
    lst[idx] = 0
    ans_idx += 1

for i in range(N):
    if i == 0:
        print('<', end='')
    if i == N-1:
        print(answer[i], end='>')
        break
    print(answer[i], end=', ')
