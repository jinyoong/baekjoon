N = int(input())
miro = list(map(int, input().split()))


def solution():
    answer = [987654321] * N
    answer[0] = 0

    for i in range(N):

        if answer[i] == 987654321:
            return -1

        for j in range(miro[i] + 1):
            if j + i >= N:
                continue

            if answer[j + i] < answer[i] + 1:
                continue
            answer[j + i] = answer[i] + 1

    return answer[-1]


print(solution())
