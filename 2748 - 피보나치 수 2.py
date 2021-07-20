fibo_list = [0, 1]

num = int(input())

if num <= 1:
    print(fibo_list[num])
else:
    while len(fibo_list) - 1 != num:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    print(fibo_list[-1])
