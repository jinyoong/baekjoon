memo = {}

for i in range(21):
    for j in range(21):
        for k in range(21):

            if i <= 0 or j <= 0 or k <= 0:
                memo[(i, j, k)] = 1

            elif i < j < k:
                memo[(i, j, k)] = memo[(i, j, k-1)] + memo[(i, j-1, k-1)] - memo[(i, j-1, k)]

            else:
                memo[(i, j, k)] = memo[(i-1, j, k)] + memo[(i-1, j-1, k)] + memo[(i-1, j, k-1)] - memo[(i-1, j-1, k-1)]


while True:
    a, b, c = map(int, input().split())

    if [a, b, c] == [-1, -1, -1]:
        break

    if a <= 0 or b <= 0 or c <= 0:
        answer = 1
    elif a > 20 or b > 20 or c > 20:
        answer = memo[(20, 20, 20)]
    else:
        answer = memo[(a, b, c)]

    print(f'w({a}, {b}, {c}) = {answer}')
