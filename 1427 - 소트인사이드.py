num = input()
num_list = [int(i) for i in num]

num_list.sort(reverse=True)

for i in range(len(num)):
    print(num_list[i], end='')