N = int(input())

numbers = set(map(int, input().split()))

M = int(input())
answer = [0] * M
targets = list(map(int, input().split()))

for i in range(M):
    if targets[i] in numbers:
        answer[i] = 1

print(*answer)
