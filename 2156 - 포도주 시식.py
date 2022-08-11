N = int(input())
wines = [int(input()) for _ in range(N)]


def solution():
    answer = [[0, 0, 0] for _ in range(N + 1)]
    # 안 마시는 경우, 마시는 경우, 2번 연속 마시는 경우

    for i in range(N):
        # answer[i + 1][0] = max(answer[i][1], answer[i][2])
        answer[i + 1][0] = max(answer[i])
        answer[i + 1][1] = wines[i] + answer[i][0]
        answer[i + 1][2] = wines[i] + answer[i][1]

    return answer


print(max(solution()[-1]))

"""
6
1000
1000
1
1
1000
1000

답 : 4000
출력 : 3001
"""
