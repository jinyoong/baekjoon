'''
i 번째 숫자와 i-1 * i 번째 숫자를 비교했을 때 곱한 값이 더 크면 i 대신 i * i-1 숫자를 놓는다
i+1 번째 숫자를 볼 때 i+1 * i 가 i+1 보다 큰 지 봐야 하는데, 만약 i+1 * i > i*1 이라는 말은
i+1 * i * i-1 > i+1 이라는 말이 된다
'''

N = int(input())

num_lst = [0.0] * N

for i in range(N):
    number = float(input())
    num_lst[i] = number

answer = num_lst[0]
for i in range(1, N):
    if num_lst[i] * num_lst[i-1] > num_lst[i]:
        num_lst[i] = num_lst[i] * num_lst[i-1]

    if num_lst[i] > answer:
        answer = num_lst[i]

temp = str(answer).split('.')
result = temp[0] + '.'
cnt = 1

for i in range(len(temp[1])):
    if i < 2:
        result += temp[1][i]
        continue

    if i == 2:
        if temp[1][i+1] >= '5':
            result += str(int(temp[1][i]) + 1)
        else:
            result += temp[1][i]
        break

print('{:0.3f}'.format(answer))
