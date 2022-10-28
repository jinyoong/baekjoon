import sys

custom_input = sys.stdin.readline

N, K = map(int, custom_input().split())
numbers = list(map(int, custom_input().split()))


def solution(belt, n, k):
    answer = 0
    count = 0
    start = 0
    on_belt = [0] * n

    while count < k:
        answer += 1
        start = (start + (2 * n - 1)) % (2 * n)

        for i in range(n - 1, 0, -1):
            on_belt[i] = on_belt[i - 1]
            on_belt[i - 1] = 0

        if on_belt[n - 1]:
            on_belt[n - 1] = 0

        for i in range(n - 1, 0, -1):
            move_idx = (start + i) % (2 * n)

            if belt[move_idx] >= 1 and not on_belt[i] and on_belt[i - 1]:
                on_belt[i] = on_belt[i - 1]
                on_belt[i - 1] = 0
                belt[move_idx] -= 1

                if belt[move_idx] == 0:
                    count += 1

        if on_belt[n - 1]:
            on_belt[n - 1] = 0

        if belt[start] >= 1:
            on_belt[0] = 1
            belt[start] -= 1

            if belt[start] == 0:
                count += 1

    return answer


print(solution(numbers, N, K))
