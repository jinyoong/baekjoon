# 고정 리스트 사용
import sys

a = int(input())

temp = [0 for i in range(a)]

input_list = []
s_index = -1

for i in range(a):
    input_list.append(sys.stdin.readline().split())
# print(input_list)

for order in input_list:
    # print('{}번째 차례입니다.'.format(input_list.index(order) + 1)
    # print('{} 명령어를 수행합니다.'.format(order[0]))
    # print('현재 s_index는 {}입니다.'.format(s_index))
    if order[0] == 'push':
        s_index += 1
        temp[s_index] = int(order[1])
    elif order[0] == 'pop':
        if temp[s_index] == 0:
            print(-1)
        else:
            print(temp[s_index])
            temp[s_index] = 0
            s_index -= 1
    elif order[0] == 'size':
        print(s_index + 1)
    elif order[0] == 'empty':
        if s_index == -1:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if temp[s_index] == 0:
            print(-1)
        else:
            print(temp[s_index])
    # print('현재 스택은 {}입니다.'.format(temp))
    # print(temp)

# 가변 리스트 사용


'''T = int(input())

temp = []
order_list = []

for i in range(T):
    order_list.append(input().split())

for order in order_list:
    if order[0] == 'push':
        temp.append(int(order[1]))
    elif order[0] == 'pop':
        if not temp:
            print(-1)
        else:
            print(temp[-1])
            temp.pop()
    elif order[0] == 'size':
        print(len(temp))
    elif order[0] == 'empty':
        if not temp:
            print(1)
        else:
            print(0)
    else:
        if not temp:
            print(-1)
        else:
            print(temp[-1])'''
