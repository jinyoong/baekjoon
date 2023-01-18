import sys

custom_input = sys.stdin.readline

N, K = map(int, custom_input().split())
numbers = list(map(int, custom_input().split()))
answer = []


def solution(start, end):

    if start >= end:
        return

    middle = (start + end) // 2
    solution(start, middle)
    solution(middle + 1, end)

    left = start
    right = middle + 1
    merge_side = []

    while left <= middle and right <= end:

        if numbers[left] < numbers[right]:
            merge_side.append(numbers[left])
            left += 1
        else:
            merge_side.append(numbers[right])
            right += 1

    while left <= middle:
        merge_side.append(numbers[left])
        left += 1

    while right <= end:
        merge_side.append(numbers[right])
        right += 1

    for i in range(start, end + 1):
        answer.append(merge_side[i - start])
        numbers[i] = merge_side[i - start]

    return


solution(0, len(numbers) - 1)

if len(answer) < K:
    print(-1)
else:
    print(answer[K - 1])
