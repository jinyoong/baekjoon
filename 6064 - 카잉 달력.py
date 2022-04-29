def solution(lst):
    M, N, x, y = lst
    result = x

    if y == N:
        y = 0

    check = {y, }

    while True:
        if result % N == y:
            return result

        if result % N in check:
            return -1

        check.add(result % N)

        result += M


T = int(input())

for _ in range(T):
    temp = list(map(int, input().split()))
    answer = solution(temp)
    print(answer)
