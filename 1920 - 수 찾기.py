import sys

input = sys.stdin.readline


def find_target(num, left, right):
    if left > right:
        return 0

    middle = (left + right) // 2

    if numbers[middle] > num:
        return find_target(num, left, middle-1)

    elif numbers[middle] < num:
        return find_target(num, middle+1, right)

    else:
        return 1


N = int(input())

numbers = sorted(list(map(int, input().split())))

M = int(input())

targets = list(map(int, input().split()))

for target in targets:
    print(find_target(target, 0, N-1))
