N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()


def permutation(count, limit, result):
    if count == limit:
        print(*result)
        return

    for i in range(N):
        if numbers[i] in result:
            continue

        permutation(count + 1, limit, result + [numbers[i]])


for k in range(N):
    permutation(1, M, [numbers[k]])
