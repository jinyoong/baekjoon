import sys
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]
answer = 987654321987654321


def solution(start, result):
    global answer
    # 한 줄에 x개의 이름이 들어가면 x - 1 만큼의 이름 사이 공간이 생기고,
    # m - 각 이름의 길이 합 + (x - 1) 만큼이 남은 공간이 된다
    width = m

    if answer <= result:
        return

    for i in range(start, n):

        new_width = width - ((names[i] + 1) if i != start else names[i])

        if new_width >= 0:
            width = new_width

            if i == n - 1:

                if answer > result:
                    answer = result
                return

            solution(i + 1, result + width ** 2)

        else:
            solution(i, result + width ** 2)
            break


def solution2():
    # n 개의 숫자를 담을 배열을 만들어 dp[i] 에는 i 번째 숫자가 줄의 맨 처음에 위치할 때의 차지하는 공간과 최소값을 저장한다.
    # 이 경우 dp[0]에 저장된 값이 전체의 최소값이 된다
    if n == 1:
        return 0

    result = [[0, 0, 0] for _ in range(n)]
    result[-1][0] = names[-1]
    result[-1][1] = 0
    result[-1][2] = 1

    for i in range(n - 2, -1, -1):
        if names[i] + result[i + 1][0] + 1 <= m:  # 뒤에 붙일 수 있는 경우
            if result[i + 1][2]:  # 바로 다음에 있던 숫자가 마지막 줄이었던 경우
                result[i][0] = names[i] + result[i + 1][0] + 1
                result[i][1] = 0
                result[i][2] = 1
            else:  # 바로 다음에 있던 숫자가 마지막 줄이 아닌 경우
                if (m - names[i] - result[i + 1][0] - 1) ** 2 < (m - names[i]) ** 2 + result[i][1]:
                    result[i][0] = names[i] + result[i + 1][0] + 1
                    result[i][1] = (m - names[i] - result[i + 1][0] - 1) ** 2
                else:
                    result[i][0] = names[i]
                    result[i][1] = (m - names[i]) ** 2 + result[i][1]
        else:
            result[i][0] = names[i]
            result[i][1] = (m - result[i][0]) ** 2

    return result


print(solution2())
