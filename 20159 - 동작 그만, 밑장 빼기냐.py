N = int(input())
numbers = list(map(int, input().split()))
temp = [0] * N
temp[0] = numbers[0]
temp[1] = numbers[1]

for i in range(2, N):
    temp[i] = temp[i - 2] + numbers[i]

answer = temp[-2]
result = 0

for i in range(N):

    if i == 0:
        result = temp[-1]
    elif i % 2:
        result = result + numbers[i - 1] - numbers[-1]
    else:
        result = result - numbers[i - 1] + numbers[-1]

    if answer < result:
        answer = result

print(answer)

"""
6
3 2 5 2 1 3

6
1 2 100 80 5 2

8
10 100 1 200 1000 89 800 2

8
9 8 3 5 3 7 8 10000
"""
