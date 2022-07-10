import sys
import collections
custom_input = sys.stdin.readline

N, M = map(int, input().split())

maps = {}
answer = []
maximum = 0

for _ in range(M):
    a, b = map(int, custom_input().split())
    maps[b] = maps.get(b, []) + [a]


def bfs(start):
    deque = collections.deque([start])
    # queue = [start for _ in range(N + 1)]
    # head = 0
    # length = 1
    check = [0 for _ in range(N + 1)]
    check[start] = 1
    result = 1

    while deque:
        parent = deque.popleft()
        # head += 1
        children = maps.get(parent, [])

        if not children:
            continue

        for child in children:
            # if answer[child]:
            #     result += answer[child]
            #     continue

            if check[child]:
                continue

            check[child] = 1
            result += 1
            deque.append(child)
            # queue[length] = child
            # length += 1

    return result


for i in range(1, N + 1):
    count = bfs(i)
    if maximum < count:
        maximum = count
        answer = [i]
    elif maximum == count:
        answer.append(i)

for ans in answer:
    print(ans, end=" ")

"""
7 6
6 7
5 7
4 6
3 6
2 5
1 5
"""

# queue = [0] * N
# head = 0
# length = 0
#
# for parent, children in maps.items():
#
#     result = 1
#
#     for child in children:
#
#         if child in answer.keys():
#             answer[parent] = answer[child] + 1
#
#         else:
#             queue[length] = child
#             result += 1
#             length += 1
#
#             while head < length:
#                 current_node = queue[head]
#                 head += 1
#
#                 if current_node not in maps.keys():
#                     continue
#
#                 next_children = maps[current_node]
#                 print(queue)
#                 for next_child in next_children:
#                     queue[length] = next_child
#                     result += 1
#                     length += 1
#
#             answer[parent] = result
#
# max_count = max(answer.values())
# result = []
# for i in range(1, N + 1):
#
#     if i not in answer.keys():
#         continue
#
#     if answer[i] == max_count:
#         result.append(i)
#
# print(*result)
