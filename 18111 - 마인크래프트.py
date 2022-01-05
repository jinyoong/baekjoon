import sys

n, m, blocks = map(int, input().split())

map_dict = {}
max_num = 0
min_num = 256
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if line[j] < min_num:
            min_num = line[j]

        if line[j] > max_num:
            max_num = line[j]

        if line[j] in map_dict.keys():
            map_dict[line[j]] += 1
        else:
            map_dict[line[j]] = 1

answer = [987654321, 0]
for height in range(min_num, max_num+1):
    append_ct = 0
    pop_ct = 0
    time = 0

    for key, value in map_dict.items():
        if key > height:
            pop_ct += (key - height) * value

        elif key < height:
            append_ct += (height - key) * value

    if pop_ct + blocks < append_ct:
        continue

    time = pop_ct * 2 + append_ct

    if time < answer[0]:
        answer = [time, height]

    elif time == answer[0]:
        answer[1] = height

print(*answer)
