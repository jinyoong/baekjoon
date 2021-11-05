def solution(idx, result, check):
    global answer

    if idx == N:
        if result < answer:
            answer = result
        return

    if result >= answer:
        return

    for i in range(3):
        if i == check:
            continue
        solution(idx+1, result+costs[idx][i], i)


# N = int(input())
# costs = [list(map(int, input().split())) for _ in range(N)]
# answer = 1000 * N
# for i in range(3):
#     solution(0, 0, i)
# print(answer)


def dp():
    temp = [[1000 * N] * 3 for _ in range(N)]
    temp[0] = costs[0]

    for i in range(1, N):
        for j in range(3):  # i 행의 j 열의 숫자를 채우기 위한 반복문
            for k in range(3):  # i-1 행의 k 열의 숫자들을 보기 위한 반복문
                if j == k:
                    continue
                value = temp[i-1][k] + costs[i][j]
                if value < temp[i][j]:
                    temp[i][j] = value
    return min(temp[-1])


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
print(dp())
