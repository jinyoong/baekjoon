a, b = map(int, input().split())

if b - 45 >= 0:
    b -= 45
    print(a, b)
else:
    b = b - 45 + 60
    if a >= 1:
        a -= 1
    else:
        a = 23
    print(a, b)