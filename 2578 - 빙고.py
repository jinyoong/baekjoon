import sys


def isbingo(lst):
    result = 0

    for i in range(5):
        if lst[i] == [1] * 5:
            result += 1

        cnt = 0
        for j in range(5):
            if lst[j][i]:
                cnt += 1

        if cnt == 5:
            result += 1

    dia_1_cnt = 0
    dia_2_cnt = 0
    for i in range(5):
        if lst[i][i]:
            dia_1_cnt += 1

        if lst[i][-i-1]:
            dia_2_cnt += 1

    if dia_1_cnt == 5:
        result += 1

    if dia_2_cnt == 5:
        result += 1

    return result


loc = [[0] * 5 for _ in range(5)]
bingo = {}

for r in range(5):
    numbers = list(map(int, sys.stdin.readline().split()))
    for c in range(5):
        number = numbers[c]
        bingo[number] = (r, c)

cnt = 0
bingo_cnt = 0
is_stop = False
for i in range(5):
    targets = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        cnt += 1
        target = targets[j]
        r, c = bingo[target]
        loc[r][c] = 1

        if isbingo(loc) == 3:
            print(cnt)
            is_stop = True
            break

    if is_stop:
        break
