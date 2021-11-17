n = int(input())
triangle = list(list(map(int, input().split())) for _ in range(n))


def solution(triangle, n):
    answer = [[0] * i for i in range(1, n+1)]

    answer[0][0] = triangle[0][0]
    col_len = 1

    for r in range(n-1):
        for c in range(col_len):
            for i in range(2):
                temp = answer[r][c] + triangle[r+1][c+i]
                if answer[r+1][c+i] < temp:
                    answer[r+1][c+i] = temp

        col_len += 1

    return max(answer[-1])


print(solution(triangle, n))
