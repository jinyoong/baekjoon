def solution(life, idx, result):
    global answer

    for i in range(idx, N):
        if visited[i]:
            continue

        if life-L[i] <= 0:
            continue

        visited[i] = 1
        solution(life-L[i], i+1, result+J[i])
        visited[i] = 0

    if answer < result:
        answer = result
        return


def solution3(life, happy):

    temp = [[-1] * 101 for _ in range(N)]
    temp[0][0] = 0
    temp[0][life[0]] = happy[0]

    for i in range(1, N):
        for j in range(101):
            if temp[i-1][j] != -1:

                temp[i][j] = temp[i-1][j]

                if j+life[i] >= 100:
                    continue

                if temp[i-1][j] + happy[i] > temp[i-1][j+life[i]]:
                    temp[i][j+life[i]] = temp[i-1][j] + happy[i]

    return max(temp[-1])


N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
visited = [0] * N
answer = 0
solution(100, 0, 0)
print(answer)
print(solution3(L, J))
