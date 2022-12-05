import sys

custom_input = sys.stdin.readline

N, K = map(int, custom_input().split())


def solution(n, k):

    if n - k < k:
        big = k
        small = n - k
    else:
        big = n - k
        small = k

    top = 1
    for i in range(n, big, -1):
        top *= i

    bottom = 1
    for i in range(1, small + 1):
        bottom *= i

    answer = top // bottom

    return answer % 10007


print(solution(N, K))
