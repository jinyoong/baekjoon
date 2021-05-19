N = input()

for i in range(int(N) + 1):
    num_sum = i
    for j in str(i):
        num_sum += int(j)
    if num_sum == int(N):
        print(i)
        break
    if i == int(N):
        print(0)
        break