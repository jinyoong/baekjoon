L = int(input())
numbers = list(map(int, input().split()))
n = int(input())

numbers.sort()


def solution():
    if n in numbers:
        return 0

    minimum = 0
    maximum = 0

    # 주어진 모든 숫자가 n 보다 큰 경우를 생각하지 못해서 틀렸었다
    for number in numbers:
        if number > n:
            maximum = number
            break
        else:
            minimum = number

    answer = 0

    for i in range(minimum+1, n+1):
        for j in range(i+1, maximum):
            if j < n:
                continue
            answer += 1

    return answer


print(solution())
