N = int(input())

person = [[] for _ in range(N)]
answer = [1] * N

for i in range(N):
    person[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            answer[i] += 1

print(*answer)
