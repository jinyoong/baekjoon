import sys

custom_input = sys.stdin.readline

N = int(custom_input())
number_map = [list(map(int, custom_input().split())) for _ in range(N)]
idx_lst = [N - 1 for _ in range(N)]

answer = 0
idx = 0

for _ in range(N):
    maximum = 0
    for i in range(N):
        number = number_map[idx_lst[i]][i]
        if maximum < number:
            idx = i
            maximum = number
    idx_lst[idx] -= 1
    answer = maximum

print(answer)
