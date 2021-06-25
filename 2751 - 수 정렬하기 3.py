# 인터넷에 있는 풀이
import sys

T = int(input())

num_list = [0] * 10001

for i in range(T):
    ind = int(sys.stdin.readline())

    num_list[ind] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# 내 풀이
import sys

T = int(input())

num_list = []

for i in range(T):
    num_list.append(int(sys.stdin.readline()))

def count_sort(li):
    num_ct = 0
    num_sort = [0 for i in range(len(li))]
    max_num = max(li)
    count_list = [0] * (max_num + 1)
    count_sum_list = [0] * (max_num + 1)
    for i in range(T):
        count_list[num_list[i]] += 1
    # print(count_list)

    count_sum_list[0] = 0

    for i in range(1, max_num + 1):
        # print('정렬할 숫자 : {} 놓아야 할 위치 : {}'.format(li[i], num_dict[li[i]] - 1))
        count_sum_list[i] = count_sum_list[i - 1] + count_list[i]

    # print(count_sum_list)

    for i in range(len(li)):
        num_sort[count_sum_list[li[i]] - 1] = li[i]
        count_sum_list[li[i]] -= 1

    answer = ''

    for i in range(len(num_sort) - 1):
        answer = answer + str(num_sort[i]) + '\n'
    answer = answer + str(num_sort[-1])
    print(answer)

count_sort(num_list)