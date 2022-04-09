n = int(input())

answer = [1] * (n+1)
answer[1] = 1

for i in range(2, n+1):
    answer[i] = (answer[i-1] + answer[i-2] * 2 % 10007) % 10007

print(answer[n])
