N = int(input())
numbers = list(map(int, input().split()))
num_dict = {}

for num in numbers:
    if num not in num_dict.keys():
        num_dict[num] = 1

    else:
        num_dict[num] += 1

M = int(input())
targets = list(map(int, input().split()))
answer = [0] * M
for i in range(M):
    answer[i] = num_dict.get(targets[i], 0)

print(*answer)
