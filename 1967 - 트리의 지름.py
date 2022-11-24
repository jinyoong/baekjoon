import sys

custom_input = sys.stdin.readline

N = int(custom_input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y, z = map(int, custom_input().split())
    tree[x].append([y, z])
answer = 0


def solution(start):
    temp = [element[:] for element in tree[start]]
    result = []

    if not temp:
        return 0

    for branch, line in temp:
        branch_result = 0
        queue = [(branch, line)]
        idx = 0
        length = 1

        while idx < length:
            current, total = queue[idx]
            idx += 1

            if not tree[current] and branch_result < total:
                branch_result = total
                continue

            for child, child_line in tree[current]:
                queue.append((child, total + child_line))
                length += 1

        result.append(branch_result)

    if len(result) == 1:
        return result[0]

    result.sort()

    return result[-1] + result[-2]


for i in range(1, N + 1):
    temp_result = solution(i)
    # print("{}를 중심으로 했을 때 가지들은 {}".format(i, temp_result))
    if answer < temp_result:
        answer = temp_result

print(answer)
