N, K = map(int, input().split())


# def solution(n, k):
#
#     visited = {n}
#     queue = [(n, 0, str(n))]
#     idx = 0
#     length = 1
#
#     while idx < length:
#         point, time, numbers = queue[idx]
#         idx += 1
#
#         if point == k:
#             print(time)
#             print(*numbers.split("/"))
#             return
#
#         for new_point in [point * 2, point - 1, point + 1]:
#
#             if new_point < 0 or new_point > 2 * k:
#                 continue
#
#             if new_point in visited:
#                 continue
#
#             queue.append((new_point, time + 1, numbers + "/" + str(new_point)))
#             length += 1
#             visited.add(new_point)
#
#
# solution(N, K)


# def solution2(n, k):
#
#     visited = {n}
#     queue = [(n, 0, "")]
#     idx = 0
#     length = 1
#
#     while idx < length:
#         point, time, operators = queue[idx]
#         idx += 1
#
#         if point == k:
#             print(time)
#             print(n, end=" ")
#
#             for operator in operators:
#
#                 if operator == "*":
#                     n *= 2
#
#                 elif operator == "-":
#                     n -= 1
#
#                 else:
#                     n += 1
#
#                 print(n, end=" ")
#
#             return
#
#         for operator, new_point in {"*": point * 2, "-": point - 1, "+": point + 1}.items():
#
#             if operator != "+" and new_point < 0:
#                 continue
#
#             if operator == "*" and new_point > 2 * k:
#                 continue
#
#             if new_point in visited:
#                 continue
#
#             queue.append((new_point, time + 1, operators + operator))
#             length += 1
#             visited.add(new_point)
#
#
# solution2(N, K)


def solution3(n, k):

    visited = {n: n}
    queue = [n]
    idx = 0
    length = 1

    while idx < length:
        point = queue[idx]
        idx += 1

        if point == k:
            result = []
            result_point = point

            while result_point != n:
                result.append(result_point)
                result_point = visited[result_point]

            print(len(result))
            result.append(n)
            print(*result[::-1])
            return

        for new_point in [point * 2, point + 1, point - 1]:

            if new_point < 0 or new_point > 200000:
                continue

            if new_point in visited.keys():
                continue

            visited[new_point] = point
            queue.append(new_point)
            length += 1


solution3(N, K)
