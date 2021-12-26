X, Y = map(int, input().split())


def rev(num):
    return int(str(num)[::-1])


print(rev(rev(X) + rev(Y)))
