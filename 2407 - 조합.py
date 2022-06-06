n, m = map(int, input().split())

if n - m < m:
    big = m
    small = n - m
else:
    big = n - m
    small = m
top_num = 1
bottom_num = 1

for i in range(n, big, -1):
    top_num *= i

for i in range(1, small + 1):
    bottom_num *= i

print(top_num // bottom_num)
