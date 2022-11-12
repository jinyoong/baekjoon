import sys

custom_input = sys.stdin.readline

N = int(custom_input())
lst = [list(custom_input().split()) for _ in range(N)]


def make_dict(key, value, dictionary):

    if key in dictionary:

        if value not in dictionary[key]:
            dictionary[key][value] = dict()

    else:
        dictionary[key] = {value: dict()}

    return dictionary


def print_ant(dictionary, depth):
    key_lst = sorted(list(dictionary.keys()))

    if not key_lst:
        return

    for key in key_lst:
        print("--" * depth + key)
        print_ant(dictionary[key], depth + 1)


def solution(ants):
    result = dict()

    for ant in ants:
        length = int(ant[0])
        temp = result

        if length == 1:
            if ant[1] not in temp:
                temp[ant[1]] = dict()
            continue

        for i in range(1, length):
            parent = ant[i]
            child = ant[i + 1]
            make_dict(parent, child, temp)
            temp = temp[parent]

    print_ant(result, 0)

    return result


solution(lst)

"""
2
3 A A A
3 A A B

5
2 A C
2 A A
3 A B A
5 A B B C E
5 A B B C D
"""
