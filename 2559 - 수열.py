N, K = map(int, input().split())

numbers = list(map(int, input().split()))

if K == 1:
    print(max(numbers))
else:
    sums = [0] * (N + 1)
    result = -100 * N
    for i in range(N):
        sums[i+1] = sums[i] + numbers[i]

    for i in range(K, N+1):
        if sums[i] - sums[i - K] > result:
            result = sums[i] - sums[i - K]

    print(result)
