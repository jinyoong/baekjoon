import sys


def double(n):

    return (n * 2) % 10000


def minus(n):

    return (n - 1) if n != 0 else 9999


def move_left(n):

    new_n = (n % 1000) * 10 + n // 1000

    return new_n


def move_right(n):

    new_n = (n % 10) * 1000 + n // 10

    return new_n


N = int(input())

for _ in range(N):
    target, goal = map(int, sys.stdin.readline().split())
    check = [0] * 10000
    queue = [(target, "")]
    check[target] = 1
    head = 0
    rear = 1

    while head < rear:
        num, result = queue[head]
        head += 1

        if num == goal:
            print(result)
            break

        for ele, alpha in [(double, "D"), (minus, "S"), (move_left, "L"), (move_right, "R")]:
            new_num, new_result = ele(num), result + alpha

            if check[new_num]:
                continue

            queue.append((new_num, new_result))
            check[new_num] = 1
            rear += 1


# def double(lst):
#     for i in range(4):
#         lst[i] *= 2
#
#     for i in range(-1, -5, -1):
#         if lst[i] >= 10:
#             if i > -4:
#                 lst[i - 1] += 1
#             lst[i] %= 10
#
#     return lst
#
#
# def minus(lst):
#     lst[-1] -= 1
#
#     for i in range(-1, -5, -1):
#         if lst[i] < 0:
#             if i > -4:
#                 lst[i - 1] -= 1
#             lst[i] = 9
#
#     return lst
#
#
# def move_left(lst):
#     res = [0] * 4
#     for i in range(3, -1, -1):
#         res[(i - 1) % 4] = lst[i]
#
#     return res
#
#
# def move_right(lst):
#     res = [0] * 4
#     for i in range(4):
#         res[(i + 1) % 4] = lst[i]
#
#     return res
#
#
# N = int(input())
#
# for _ in range(N):
#     target, goal = sys.stdin.readline().split()
#     target_lst = list(map(int, target))
#     goal_lst = list(map(int, goal))
#
#     d_lst = [0] * (4 - len(target_lst)) + target_lst
#     g_lst = [0] * (4 - len(goal_lst)) + goal_lst
#     check = set()
#
#     queue = [""]
#     check_dict = {"": d_lst}
#     head = 0
#     rear = 1
#     answer = ""
#
#     while head < rear:
#         num_lst, result = check_dict[queue[head]], queue[head]
#         head += 1
#
#         if num_lst == g_lst:
#             answer = result
#             break
#
#         for ele, alpha in [(double, "D"), (minus, "S"), (move_left, "L"), (move_right, "R")]:
#             new_lst = ele(num_lst[:])
#             new_result = result + alpha
#             if new_result in check_dict.keys():
#                 continue
#
#             queue.append(new_result)
#             check_dict[new_result] = new_lst
#             rear += 1
#
#     print(answer)
