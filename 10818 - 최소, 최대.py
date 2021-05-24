N = int(input())

num_list = list(map(int, input().split()))

min_num = num_list[0]
max_num = num_list[0]

for i in range(1, N):
    if min_num >= num_list[i]:
        min_num = num_list[i]
    if max_num <= num_list[i]:
        max_num = num_list[i]

print(min_num, max_num)