import sys

input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

sorted_lst = sorted(lst, key=lambda x: x[0])

answer = [sorted_lst[0][1]]

for ele in sorted_lst[1:]:
    target = ele[1]

    if target < answer[0]:
        answer[0] = target
        continue

    if target > answer[-1]:
        answer.append(target)
        continue

    for i in range(1, len(answer)):
        if answer[i-1] < target < answer[i]:
            answer[i] = target
            break

print(N - len(answer))
