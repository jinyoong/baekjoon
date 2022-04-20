import sys

input = sys.stdin.readline


def minus(x):
    return int(x) - 1


N, M = map(int, input().split())
numbers = [[] for _ in range(N)]

for i in range(N):
    numbers[i] = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(1, N):
        numbers[i][j] += numbers[i][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(minus, input().split())
    result = 0

    for r in range(x1, x2+1):
        if y1 == 0:
            result += numbers[r][y2]
        else:
            result += numbers[r][y2] - numbers[r][y1 - 1]

    print(result)
