N = int(input())
M = N

answer = 1

if N < 10:
    num_sum = 0 + N
    new_num = N * 10 + num_sum
else:
    num_sum = int(str(N)[0]) + int(str(N)[1])
    new_num = (N % 10) * 10 + (num_sum % 10)

while new_num != M:
    answer += 1
    if new_num < 10:
        num_sum = 0 + new_num
        new_num = new_num * 10 + num_sum
    else:
        num_sum = int(str(new_num)[0]) + int(str(new_num)[1])
        new_num = (new_num % 10) * 10 + (num_sum % 10)

print(answer)