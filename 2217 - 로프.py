N = int(input())
num_lst = [int(input()) for _ in range(N)]

num_lst.sort()

answer = 0
for i in range(N):
    temp = num_lst[i] * (N - i)
    if answer < temp:
        answer = temp

print(answer)
