import sys

T = int(input())

answer = 0
num_list = []

for i in range(T):
    temp = int(sys.stdin.readline())
    if temp != 0:
        num_list.append(temp)
    else:
        num_list.pop()

for num in num_list:
    answer += int(num)

print(answer)