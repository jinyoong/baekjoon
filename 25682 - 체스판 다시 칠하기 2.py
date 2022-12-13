import sys

custom_input = sys.stdin.readline

N, M, K = map(int, custom_input().split())
lst = [list(custom_input().rstrip()) for _ in range(N)]


def solution(board, n, m, k):
    answer = 987654321

    result1 = make_board(board, ["B", "W"], n, m)
    result2 = make_board(board, ["W", "B"], n, m)

    check = []
    for c in range(k, m + 1):
        for r in range(k, n + 1):

            check.append([r, c])

    for cr, cc in check:

            temp1 = count_color(result1, cr, cc, k)
            temp2 = count_color(result2, cr, cc, k)

            if answer > temp1:
                answer = temp1

            if answer > temp2:
                answer = temp2

    return answer


def make_board(board, case, n, m):
    result = [[0] * (m + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        count = 0 if r % 2 else 1

        for c in range(1, m + 1):

            if board[r - 1][c - 1] == case[count % 2]:
                result[r][c] = result[r][c - 1]
            else:
                result[r][c] = result[r][c - 1] + 1

            count += 1

    return result


def count_color(cut_board, n, m, k):
    result = 0

    for r in range(k):
        result += cut_board[n - r][m] - cut_board[n - r][m - k]

    return result


def solution2(board, n, m, k):
    answer = 987654321
    result = [[[0, 0, 0, 0] for _ in range(m + 1)]for _ in range(n + 1)]
    case1 = ["B", "W"]
    case2 = ["W", "B"]

    for r in range(1, n + 1):
        count = 0 if r % 2 else 1

        for c in range(1, m + 1):

            if board[r - 1][c - 1] == case1[count % 2]:
                result[r][c][0] = result[r][c - 1][0]
            else:
                result[r][c][0] = result[r][c - 1][0] + 1

            if board[r - 1][c - 1] == case2[count % 2]:
                result[r][c][1] = result[r][c - 1][1]
            else:
                result[r][c][1] = result[r][c - 1][1] + 1

            if c >= k:
                result[r][c][2] = result[r][c][0] - result[r][c - k][0] + result[r - 1][c][2]
                result[r][c][3] = result[r][c][1] - result[r][c - k][1] + result[r - 1][c][3]

            count += 1

    for r in range(n + 1):
        print(*result[r])

    for r in range(k, n + 1):
        for c in range(k, m + 1):

            temp1 = result[r][c][2] - result[r - k][c][2]
            temp2 = result[r][c][3] - result[r - k][c][3]

            if answer > temp1:
                answer = temp1

            if answer > temp2:
                answer = temp2

    return answer


def solution3(board, case, n, m, k):
    answer = 987654321
    result = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

    for r in range(1, n + 1):
        count = 0 if r % 2 else 1

        for c in range(1, m + 1):

            if board[r - 1][c - 1] == case[count % 2]:
                result[r][c][0] = result[r][c - 1][0]
            else:
                result[r][c][0] = result[r][c - 1][0] + 1

            if c >= k:
                result[r][c][1] = result[r][c][0] - result[r][c - k][0] + result[r - 1][c][1]

            count += 1

    for c in range(k, m + 1):
        for r in range(k, n + 1):

            temp = result[r][c][1] - result[r - k][c][1]

            if answer >= temp:
                answer = temp

    return answer


def solution4(board, case, n, m, k):
    answer = 987654321
    result = [[0] * (m + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        count = 0 if r % 2 else 1

        for c in range(1, m + 1):

            if board[r - 1][c - 1] == case[count % 2]:
                plus = 0
            else:
                plus = 1

            result[r][c] = result[r - 1][c] + result[r][c - 1] - result[r - 1][c - 1] + plus

            count += 1

    for r in range(k, n + 1):
        for c in range(k, m + 1):

            temp = result[r][c] - result[r - k][c] - result[r][c - k] + result[r - k][c - k]

            if answer > temp:
                answer = temp

    return answer


# print(solution(lst, N, M, K))
# print(solution2(lst, N, M, K))
# print(min(solution3(lst, ["B", "W"], N, M, K), solution3(lst, ["W", "B"], N, M, K)))
print(min(solution4(lst, ["B", "W"], N, M, K), solution4(lst, ["W", "B"], N, M, K)))
