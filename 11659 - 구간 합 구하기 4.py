import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
answers = [0] * (N + 1)

for i in range(N):
    answers[i+1] = answers[i] + numbers[i]

for i in range(1, M+1):
    s, f = map(int, input().split())
    print(answers[f] - answers[s-1])
