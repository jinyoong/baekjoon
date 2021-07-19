# 0 = 1 0
# 1 = 0 1
# 2 = 1 1
# 3 = 1 2
# 4 = 2 3
# 5 = 3 5
zero_one = [[1, 0], [0, 1]]

def fibo_one(n):
    if n <= len(zero_one)-1:
        print(*zero_one[n])
    else:
        for i in range(n - len(zero_one) + 1):
            zero_one.append([zero_one[-2][0] + zero_one[-1][0], zero_one[-2][1] + zero_one[-1][1]])
        print(*zero_one[-1])

T = int(input())
fibo_list = []
for i in range(T):
    fibo_num = int(input())
    fibo_one(fibo_num)