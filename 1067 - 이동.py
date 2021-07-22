T = int(input())
X_list = list(map(int, input().split()))
Y_list = list(map(int, input().split()))

max_num = 0
for i in range(-1, -T-1, -1):
    total = 0
    for j in range(T):
        total += X_list[j] * Y_list[i+j]
    if max_num < total:
        max_num = total
print(max_num)