import sys

custom_input = sys.stdin.readline

N, M = map(int, custom_input().split())
lst = list(map(int, custom_input().split()))


def solution(numbers, n, m):
    """
    (a % n + b % n) % n = (a + b) % n
    """
    answer = 0
    sum_lst = [0] * (n + 1)
    for i in range(n):
        sum_lst[i + 1] = sum_lst[i] + numbers[i]

    for i in range(n, 0, -1):
        standard = sum_lst[i]

        for j in range(i - 1, -1, -1):
            target = sum_lst[j]

            if (standard - target) % m == 0:
                answer += 1

    return answer


print(solution(lst, N, M))


def solution2(numbers, n, m):
    answer = 0
    sum_lst = [0] * (n + 1)
    remains = [0] * m
    remains[0] = 1

    for i in range(n):
        number = (sum_lst[i] % m + numbers[i] % m) % m
        sum_lst[i + 1] = number
        remains[number] += 1

    for remain in remains:

        if remain < 2:
            continue

        answer += (remain * (remain - 1)) // 2

    return answer


print(solution2(lst, N, M))
