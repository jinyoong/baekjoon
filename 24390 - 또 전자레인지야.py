M, S = map(int, input().split(":"))
t = M * 60 + S


def solution(time):
    answer = 0

    answer += time // 600
    time = time % 600

    answer += time // 60
    time = time % 60

    if time >= 30:
        answer += time // 30
        time = time % 30
        answer += time // 10

    else:
        answer += time // 10
        answer += 1

    return answer


print(solution(t))
