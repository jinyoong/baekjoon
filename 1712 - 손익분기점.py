a, b, c = map(int, input().split())

sale_ct = 0
if b >= c:
    sale_ct = -1
else:
    sale_ct = (a // (c - b)) + 1
print(sale_ct)