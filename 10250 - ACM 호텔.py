T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    hori = N // H + 1
    verti = N % H
    if verti == 0:
        verti = H
        hori -= 1
    print('{0}{1:0>2}'.format(verti, hori))