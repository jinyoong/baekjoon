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

    result = [0 for _ in range(n)]

    for i in range(n - 2, -1, -1):
        number = (m - names[i]) ** 2 + result[i + 1]
        # names[i] 이름을 새로운 줄의 맨 처음에 위치시키는 경우
        # names[i] 가 위치한 줄 뒤에는 names[i + 1] 로 시작하는 줄이 위치

        length = names[i]
        for j in range(i + 1, n):
            # names[i] 이름 뒤에 이름을 이어 붙이는 경우
            # names[i] ~ names[j] 까지의 이름이 한 줄에 위치한 경우, 그 다음 줄에는 names[j + 1] 로 시작하는 줄이 위치

            length += 1 + names[j]
            if length > m:
                break

            if j == n - 1:  # 맨 마지막 이름까지 모두 이어 붙일 수 있다면, 무조건 0 이 된다
                number = 0
                break

            new_number = (m - length) ** 2 + result[j + 1]

            if new_number < number:
                number = new_number

        result[i] = number

    return result[0]


print(solution2())
