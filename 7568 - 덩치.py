import sys

T = int(input())

big_list = []
answer = []

for i in range(T):
    big_list.append(sys.stdin.readline().split())

for j in range(T):
    temp = big_list.copy()
    temp[0], temp[j] = big_list[j], big_list[0]
    temp_ct = 0

    # print('현재 덩치 등수를 구할 사람은 {}입니다.'.format(temp[0]))
    for k in range(1, T):
        if temp[0][0] < temp[k][0] and temp[0][1] < temp[k][1]:
            # print('{}이 {}보다 덩치가 큽니다.'.format(temp[k], temp[0]))
            temp_ct += 1
    answer.append(temp_ct + 1)

print(*answer)
