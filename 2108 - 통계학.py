import sys

input = sys.stdin.readline

T = int(input())

num_list = []
num_sum = 0
max_num = 0
min_num = 0
num_dict = {}

for i in range(T):
    temp = int(input())
    if i == 0:
        max_num = temp
        min_num = temp
        num_list.append(temp)
        num_dict[temp] = 1
        num_sum += temp
    else:
        if temp > max_num:
            max_num = temp
        elif temp < min_num:
            min_num = temp
        num_list.append(temp)
        num_sum += temp
        if temp not in num_dict.keys():
            num_dict[temp] = 1
        else:
            num_dict[temp] += 1

num_list.sort()
many_cnt = max(num_dict.values())
many_nums = []
for num, cnt in num_dict.items():
    if cnt == many_cnt:
        many_nums.append(num)

many_nums.sort()

print('%0.0f' % (num_sum/T))
print(num_list[T//2])
if len(many_nums) == 1:
    print(many_nums[0])
else:
    print(many_nums[1])
print(max_num - min_num)
