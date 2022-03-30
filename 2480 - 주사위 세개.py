a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or c == a:
    temp = 0
    if a == b:
        temp = a
    elif b == c:
        temp = b
    else:
        temp = c
    print(1000 + temp * 100)
else:
    print(max(a, b, c) * 100)
