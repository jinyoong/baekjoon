T = int(input())

temp = []
goal_list = []
ct = 0
answer = []
for j in range(T):
    goal_list.append(int(input()))

# print(goal_list)
for num in goal_list:
    '''print('{}를 넣기 위한 작업을 살펴봅니다.'.format(num))
    print(ct)
    print(temp)'''
    if not temp:
        ct += 1
        temp.append(ct)
        answer.append('+')
    while num != temp[-1]:
        ct += 1
        temp.append(ct)
        answer.append('+')
        if ct > T:
            break
    temp.pop()
    answer.append('-')
    if ct > T:
        answer = ['NO']
        break

for ans in answer:
    print(ans)