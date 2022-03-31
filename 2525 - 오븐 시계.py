a, b = map(int, input().split())
c = int(input())

temp = a * 60 + b + c
h = temp // 60
if h >= 24:
    h -= 24
print(h, temp % 60)
