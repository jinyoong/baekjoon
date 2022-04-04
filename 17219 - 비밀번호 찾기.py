import sys

N, M = map(int, input().split())

passwords = {}
answer = ['' for _ in range(M)]

for _ in range(N):
    site, password = sys.stdin.readline().split()
    passwords[site] = password

for i in range(M):
    answer[i] = passwords[sys.stdin.readline().rstrip()]

for ans in answer:
    print(ans)
