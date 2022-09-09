import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[987654321] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a - 1][b - 1] = min(bus[a - 1][b - 1], c)


def solution(result):

    for i in range(n):  # 경유지
        for j in range(n):  # 출발지
            for k in range(n):  # 목적지
                if j == k:
                    bus[j][k] = 0
                else:
                    bus[j][k] = min(bus[j][k], bus[j][i] + bus[i][k])

    return result


answer = solution(bus)
for r in range(n):
    for c in range(n):
        if c == n - 1:
            print(answer[r][c] % 987654321)
        else:
            print(answer[r][c] % 987654321, end=" ")
