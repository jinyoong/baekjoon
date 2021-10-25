def solution(result, idx):
    global answer

    if result > M or result < 0:
        return

    if idx == N:
        if result > answer:
            answer = result
        return

    if result+V[idx] <= M:
        solution(result+V[idx], idx+1)
    if result-V[idx] >= 0:
        solution(result-V[idx], idx+1)


def solution2():

    temp = [[0] * (M+1) for _ in range(N+1)]

    temp[0][S] = 1

    for i in range(1, N+1):

        if temp[i-1] == [0] * (M+1):
            return -1

        for j in range(M+1):

            if not temp[i-1][j]:
                continue

            if j + V[i] <= M and not temp[i][j + V[i]]:
                temp[i][j + V[i]] = 1

            if 0 <= j - V[i] and not temp[i][j - V[i]]:
                temp[i][j - V[i]] = 1

    ans = -1

    for i in range(M, -1, -1):
        if temp[-1][i]:
            ans = i
            break

    return ans


N, S, M = map(int, input().split())
V = [0] + list(map(int, input().split()))
# solution(S, 0)
print(solution2())
