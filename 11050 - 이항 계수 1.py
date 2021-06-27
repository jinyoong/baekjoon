x, y = map(int, input().split())

n = 1
k = 1

for i in range(x, x-y, -1):
    n *= i

for i in range(1, y+1):
    k *= i

print(n//k)
