A = input()
B = input()


def solution(standard, target):
    dp = [["" for _ in range(len(target) + 1)] for _ in range(len(standard) + 1)]

    for i in range(len(standard)):
        standard_alpha = standard[i]

        for j in range(len(target)):
            target_alpha = target[j]

            if standard_alpha == target_alpha:
                dp[i + 1][j + 1] = dp[i][j] + standard_alpha
            else:
                if len(dp[i + 1][j]) < len(dp[i][j + 1]):
                    dp[i + 1][j + 1] = dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]

    return dp[-1][-1]


answer = solution(A, B)
if answer:
    print(len(answer))
    print("".join(answer))
else:
    print(0)
