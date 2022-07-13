# N = int(input())
# numbers = [list(map(int, input().split())) for _ in range(N)]
# maximum = 0
# minimum = 987654321
#
#
# def solution(r, c, result):
#     global maximum, minimum
#
#     nr = r + 1
#
#     for i in range(-1, 2):
#         nc = c + i
#
#         if nc < 0 or nc >= N:
#             continue
#
#         if nr == N:
#             if result > maximum:
#                 maximum = result
#
#             if result < minimum:
#                 minimum = result
#             return
#
#         solution(nr, nc, result + numbers[nr][nc])
#
#
# for col in range(3):
#     solution(-1, col, 0)
#
#
# def solution2():
#     before_max = numbers[0]
#     before_min = numbers[0]
#
#     max_result = [0] * N
#     min_result = [0] * N
#
#     for r in range(1, N):
#         for c in range(3):
#             max_temp = 0
#             min_temp = 10
#             for i in range(-1, 2):
#
#                 if c + i < 0 or c + i >= N:
#                     continue
#
#                 max_num = before_max[c + i]
#                 min_num = before_min[c + i]
#
#                 if max_temp < max_num:
#                     max_temp = max_num
#                 if min_temp > min_num:
#                     min_temp = min_num
#
#             max_result[c] = numbers[r][c] + max_temp
#             min_result[c] = numbers[r][c] + min_temp
#
#         before_max = max_result[:]
#         before_min = min_result[:]
#
#     return max(max_result), min(min_result)


def solution3():
    n = int(input())

    before_max = [0, 0, 0]
    before_min = [0, 0, 0]

    max_result = [0, 0, 0]
    min_result = [0, 0, 0]

    for _ in range(n):
        left, middle, right = map(int, input().split())

        for i in range(3):
            if i == 0:
                max_result[i] = left + max(before_max[:2])
                min_result[i] = left + min(before_min[:2])
            elif i == 1:
                max_result[i] = middle + max(before_max)
                min_result[i] = middle + min(before_min)
            else:
                max_result[i] = right + max(before_max[1:])
                min_result[i] = right + min(before_min[1:])

        for i in range(3):
            before_max[i] = max_result[i]
            before_min[i] = min_result[i]

    return max(max_result), min(min_result)


# print(maximum, minimum)
# print(*solution2())
print(*solution3())
