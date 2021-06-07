x, y, w, h = map(int, input().split())

horizon_len = 0

if x <= w - x:
    horizon_len = x
else:
    horizon_len = w - x

vertical_len = 0

if y <= h - y:
    vertical_len = y
else:
    vertical_len = h - y

min_len = 0

if horizon_len <= vertical_len:
    min_len = horizon_len
else:
    min_len = vertical_len

print(min_len)