import sys

N, M = map(int, input().split())
lists = [''] * (N+1)
p_dict = {}

for i in range(N):
    p = sys.stdin.readline().rstrip()
    lists[i+1] = p
    p_dict[p] = i+1

for i in range(M):
    t = sys.stdin.readline().rstrip()
    if t.isdigit():
        print(lists[int(t)])
    else:
        print(p_dict[t])
