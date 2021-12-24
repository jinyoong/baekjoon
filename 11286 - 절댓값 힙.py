import sys

input = sys.stdin.readline


def heap_push(lst, idx, x):
    lst[idx] = x
    temp = idx
    while temp > 1:
        if abs(lst[temp//2]) > abs(lst[temp]) or (abs(lst[temp//2]) == abs(lst[temp]) and lst[temp//2] > lst[temp]):
            lst[temp//2], lst[temp] = lst[temp], lst[temp//2]
            temp //= 2
        else:
            break

    return idx+1


def heap_pop(lst, idx):
    result = lst[1]
    idx -= 1
    lst[1], lst[idx] = lst[idx], lst[1]
    lst[idx] = 2147483649

    temp = 1
    while temp < idx:
        p = lst[temp]
        abs_p = abs(p)
        if temp * 2 >= idx:
            break

        if temp * 2 + 1 <= idx:
            c1, c2 = lst[temp * 2], lst[temp * 2 + 1]
            abs_c1, abs_c2 = abs(c1), abs(c2)

            if abs_c1 < abs_c2:
                if abs_p < abs_c1 or (abs_p == abs_c1 and p < c1):
                    break
                lst[temp], lst[temp * 2] = lst[temp * 2], lst[temp]
                temp = temp * 2

            elif abs_c1 > abs_c2:
                if abs_p < abs_c2 or (abs_p == abs_c2 and p < c2):
                    break
                lst[temp], lst[temp * 2 + 1] = lst[temp * 2 + 1], lst[temp]
                temp = temp * 2 + 1

            elif abs_c1 == abs_c2:
                if c1 <= c2 and (abs_p > abs_c1 or (abs_p == abs_c1 and p > c1)):
                    lst[temp], lst[temp * 2] = lst[temp * 2], lst[temp]
                    temp = temp * 2
                elif c1 > c2 and (abs_p > abs_c2 or (abs_p == abs_c2 and p > c2)):
                    lst[temp], lst[temp * 2 + 1] = lst[temp * 2 + 1], lst[temp]
                    temp = temp * 2 + 1
                else:
                    break

            else:
                break

        else:
            c = lst[temp * 2]

            if abs_p < abs(c) or (abs_p == abs(c) and p < c):
                break

            lst[temp], lst[temp * 2] = lst[temp * 2], lst[temp]
            temp = temp * 2

    return result, idx


N = int(input())

heap = [2147483649] * (N + 1)
idx = 1

for _ in range(N):
    num = int(input())

    if num == 0 and idx == 1:
        print(0)

    elif num == 0 and idx > 1:
        result, idx = heap_pop(heap, idx)
        print(result)

    else:
        idx = heap_push(heap, idx, num)


# from heapq import heappush, heappop
#
#
# heap = []
# N = int(input())
#
# for _ in range(N):
#     num = int(input())
#
#     if num == 0:
#         if heap:
#             print(heappop(heap)[1])
#         else:
#             print(0)
#
#     else:
#         heappush(heap, [abs(num), num])

'''
6
1
-2
2
0
0
0
답
1
-2
2

4
1
1
-1
0
답
-1
'''