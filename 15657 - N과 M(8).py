N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()


def solution(idx, cnt, result):
    if cnt == M:
        print(*result)
        return

    for i in range(idx, N):
        solution(i, cnt+1, result+[numbers[i]])


solution(0, 0, [])
