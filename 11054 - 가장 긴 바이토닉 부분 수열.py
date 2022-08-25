N = int(input())
numbers = list(map(int, input().split()))
answer = 0
ascending = [1] * N
descending = [1] * N

for i in range(1, N):
    max_count = 0
    for j in range(i, -1, -1):

        if numbers[j] >= numbers[i]:
            continue

        if ascending[j] <= max_count:
            continue

        max_count = ascending[j]

    ascending[i] = max_count + 1

for i in range(N - 2, -1, -1):
    max_count = 0
    for j in range(i, N):

        if numbers[j] >= numbers[i]:
            continue

        if descending[j] <= max_count:
            continue

        max_count = descending[j]

    descending[i] = max_count + 1


for i in range(N):
    if answer < ascending[i] + descending[i]:
        answer = ascending[i] + descending[i]

print(answer - 1)
