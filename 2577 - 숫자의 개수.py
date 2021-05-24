num = 1

for i in range(3):
    num *= int(input())

for i in range(10):
    print(str(num).count(str(i)))