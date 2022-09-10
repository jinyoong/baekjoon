import sys
limit_number = 1000000000
sys.setrecursionlimit(limit_number)

n = int(input())
# memo = [0] * (n + 1)
# memo[1] = 1
#
#
# def solution(target):
#
#     if target <= 1:
#         return target
#
#     if memo[target]:
#         return memo[target]
#
#     result = (solution(target - 1) % 1000000007 + solution(target - 2) % 1000000007) % 1000000007
#     memo[target] = result
#     return result
#
#
# print(solution(n))


def solution2(num):
    alpha = beta = 1

    if num == 1:
        return 1

    while num != 2:
        temp = alpha
        alpha = (alpha + beta) % 1000000007
        beta = temp % 1000000007
        num -= 1

    return alpha


# print(solution2(n))


def solution3(num, r):

    if num == 2:
        left, new_right = 1, 2
    elif num == 1:
        left, new_right = 1, 1
    elif num == 0:
        left, new_right = 0, 0
    else:
        before_left, right = solution3(num - 2, r)
        left = (before_left + right) % r
        new_right = (left + right) % r

    return left, new_right


# print(solution3(n, 1000000007)[0])


def solution4(num):
    basic = [[1, 1], [1, 0]]

    if num == 0:
        return [[0, 0], [0, 0]]

    if num <= 1:
        return basic

    matrix = solution4(num // 2)

    if num % 2:
        half_result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    half_result[i][j] += (matrix[i][k] * matrix[k][j]) % 1000000007
                half_result[i][j] %= 1000000007

        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (half_result[i][k] * basic[k][j]) % 1000000007
                result[i][j] %= 1000000007

        return result

    else:
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (matrix[i][k] * matrix[k][j]) % 1000000007
                result[i][j] %= 1000000007

        return result


print(solution4(n))
'''     
10 = 9 8
8 = 7 6
6 = 5 4
4 = 3 2
2 = 1 0
'''
