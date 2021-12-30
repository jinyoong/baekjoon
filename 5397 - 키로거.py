import sys

input = sys.stdin.readline


def find_password(input_lst):
    cursor = 0
    len_pw = 0
    result = [''] * len(input_lst)
    for ele in input_lst:

        if ele == '<':
            for idx in range(len_pw, min(-1, cursor-1), -1):
                result[idx+1] = result[idx]
            if cursor:
                cursor -= 1
            continue

        if ele == '>':
            if cursor < len_pw:
                cursor += 1
            continue

        if ele == '-':
            if cursor:
                cursor -= 1
            result[cursor] = ''
            continue

        result[cursor] = ele
        cursor += 1
        len_pw += 1

    return ''.join(result)


N = int(input())

for _ in range(N):
    input_str = str(input())
    print(find_password(input_str))
