import sys

def min_heap_push(x):
    idx = len(lst)
    lst.append(x)

    while idx // 2 >= 1:
        if lst[idx // 2] > lst[idx]:
            lst[idx // 2], lst[idx] = lst[idx], lst[idx // 2]
            idx //= 2
        else:
            break


def min_heap_pop():
    idx = len(lst)

    if idx == 1:
        return 0

    lst[1], lst[idx - 1] = lst[idx - 1], lst[1]
    result = lst[idx - 1]
    lst.pop(-1)
    idx -= 2
    p = 1

    while p * 2 <= idx:
        c1, c2 = p * 2, p * 2 + 1
        if c2 > idx:
            c = c1
        else:
            if lst[c1] <= lst[c2]:
                c = c1
            else:
                c = c2

        if lst[p] > lst[c]:
            lst[p], lst[c] = lst[c], lst[p]
        p = c

    return result


N = int(input())

lst = [0]

for _ in range(N):
    num = int(sys.stdin.readline()) * -1
    if num:
        min_heap_push(num)
    else:
        print(min_heap_pop() * -1)
