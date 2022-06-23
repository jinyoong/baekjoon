n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
answer = 0

num_set = set(numbers)
for i in range(n - 1):
    num_set.remove(numbers[i])
    if (x - numbers[i]) in num_set:
        answer += 1

print(answer)
