N = input()
F = int(input())

num = N[:-2]

for i in range(0, 100):
    if i <= 9:
        add_num = '0' + str(i)
    else:
        add_num = str(i)
    if int(num + add_num) % F == 0:
        print(add_num)
        break