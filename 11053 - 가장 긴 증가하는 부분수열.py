N = int(input())
numbers = list(map(int, input().split()))


def solution():
    result = [1] * N

    for i in range(N):
        max_temp = 0
        for j in range(i, -1, -1):
            if numbers[j] < numbers[i] and max_temp < result[j]:
                max_temp = result[j]
        result[i] = max_temp + 1

    return result


ans = solution()
print(max(ans))

#
# answer = []
#
# for i in range(N):
#
#     if not answer:
#         answer.append(numbers[i])
#
#     else:
#         if answer[-1] < numbers[i]:
#             answer.append(numbers[i])
#         else:
#             for j in range(1, len(answer)):
#                 if answer[j - 1] < numbers[i] < answer[j]:
#                     answer[j - 1] = numbers[i]
#                     break
#     print(answer)
#
# print(len(answer))
