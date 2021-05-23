T, a = map(int, input().split())

num_list = list(map(int, input().split()))
answer = []

for i in num_list:
    if a > i:
        answer.append(i)
print(*answer)
