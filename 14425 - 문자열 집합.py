import sys

input = sys.stdin.readline

N, M = map(int, input().split())

str_set = set()
for _ in range(N):
    str_set.add(input())

answer = 0
for _ in range(M):
    target = input()
    if target in str_set:
        answer += 1

print(answer)
