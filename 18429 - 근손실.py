N, K = map(int, input().split())

kits = list(map(int, input().split()))
answer = 0


def solution(weight, result):
    global answer
    if len(result) == N:
        answer += 1
        return

    for i in range(N):
        if i in result:
            continue

        if weight + kits[i] - K < 500:
            continue

        solution(weight + kits[i] - K, result + [i])


for idx in range(N):
    if 500 + kits[idx] - K < 500:
        continue
    solution(500 + kits[idx] - K, [idx])

print(answer)
