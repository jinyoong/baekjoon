import sys

input = sys.stdin.readline


def b_to_d(num):
    result = 0
    for i in range(8):
        if not int(num[i]):
            continue
        result += int(num[i]) * 2 ** (8-i-1)

    return result


def d_to_b(num):
    result = ''
    while num >= 2:
        print(num)
        x, y = divmod(num, 2)
        num = x
        result = str(y) + result
    result = str(num) + result

    result = '0' * (8 - len(result)) + result

    return result


memory = []
