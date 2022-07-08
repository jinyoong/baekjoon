N = int(input())

consulting = [list(map(int, input().split())) for _ in range(N)]
consulting += [[0, 0]]
temp = [0] * (N + 1)
answer = 0


def solution2():
    for idx in range(N - 1, -1, -1):
        day, pay = consulting[idx]

        if idx + day > N:
            temp[idx] = temp[idx + 1]
            # 위 코드가 없으면 0으로 초기화된 상태로 있기 때문에 잘못된 답이 나오게 된다.
            continue

        # if temp[idx + day] < temp[idx + day] + pay:
        #     temp[idx + day] = temp[idx + day] + pay

        temp[idx] = max(temp[idx + day] + pay, temp[idx + 1])

        # print(temp)

    return max(temp)


print(solution2())


# def solution(start, result):
#     global answer
#
#     for j in range(start, 0, -1):
#         day, pay = consulting[j]
#
#         if j + day == start:
#             solution(j, result + pay)
#     else:
#         if answer < result:
#             answer = result
#
#
# for i in range(N, 0, -1):
#     d, p = consulting[i]
#     if i + d == N + 1:
#         solution(i, p)
#     else:
#         solution(i, 0)
#
# print(answer)
