num_list = []
answer = 0

for i in range(10):
    a = int(input())
    if a % 42 not in num_list:
        num_list.append(a % 42)
        answer += 1
print(answer)