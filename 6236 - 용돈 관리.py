N, M = map(int, input().split())
amounts = [int(input()) for _ in range(N)]

answer = 0
minimum = max(amounts)
maximum = minimum * N

while minimum <= maximum:

    count = 1
    middle = (minimum + maximum) // 2
    wallet = middle

    for amount in amounts:

        if wallet < amount:
            wallet = middle
            count += 1

        wallet -= amount

    if count > M:
        minimum = middle + 1
    else:
        maximum = middle - 1
        answer = middle

print(answer)
