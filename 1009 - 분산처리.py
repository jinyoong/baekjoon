def boonsan(a, b):
    if a % 10 == 0:
        return 10
    else:
        temp = []
        for i in range(1, 10):
            if a ** i % 10 not in temp:
                temp.append(a ** i % 10)
            else:
                break
        new_b = b % len(temp) - 1
        return temp[new_b]

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(boonsan(a, b))