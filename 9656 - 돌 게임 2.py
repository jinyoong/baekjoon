n = int(input())

game = ['SK', 'CY']
idx = 0
while n != 0:
    if n >= 4:
        n -= 3
    else:
        n -= 1
    idx = (idx + 1) % 2

print(game[idx])
