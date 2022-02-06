import sys


def solution(left, right):
    global answer
    middle = (left + right) // 2

    if middle == answer:
        return answer

    answer = middle

    cnt = 0
    for line in lines:
        if middle == 0:
            cnt += line
        else:
            cnt += line // middle

    if cnt < N:
        return solution(left, middle-1)

    elif cnt >= N:
        return solution(middle+1, right)


K, N = map(int, input().split())
lines = [0] * K
maximum = 0
answer = -1
for i in range(K):
    line = int(sys.stdin.readline())

    if maximum < line:
        maximum = line

    lines[i] = line

print(solution(0, maximum))

"""
4 4
4
1
5
5

4 4
99
99
99
99

4 4
100
100
100
100
"""