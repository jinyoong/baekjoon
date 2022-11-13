import sys

custom_input = sys.stdin.readline

N, K = map(int, custom_input().split())
lst = [list(map(int, custom_input().split())) for _ in range(N)]


def solution(n, k, input_list):
    answer = 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            weight, value = input_list[i - 1]
            idx = max(j - weight, 0)

            if j < weight:
                dp[i][j] = dp[i - 1][j]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][idx] + value)

            if answer < dp[i][j]:
                answer = dp[i][j]

    return answer


print(solution(N, K, lst))
