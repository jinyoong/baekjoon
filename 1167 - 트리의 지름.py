V = int(input())
input_tree = [[] for _ in range(V + 1)]
answer = 0

for _ in range(V):
    input_lst = list(map(int, input().split()))
    s = input_lst[0]
    for i in range(1, len(input_lst) - 1, 2):
        e, l = input_lst[i], input_lst[i + 1]
        input_tree[s].append((e, l))


def solution(node, tree):
    global answer
    result = 0
    visited = {node, }
    queue = [(node, 0)]
    idx = 0
    finish = 1

    while idx < finish:
        start, before = queue[idx]
        idx += 1

        end_lst = tree[start]

        for ele in end_lst:

            end, length = ele
            total = before + length

            if end in visited:
                continue

            queue.append((end, total))
            finish += 1
            visited.add(end)

            if answer < total:
                result = end
                answer = total

    return result


temp_node = solution(1, input_tree)
solution(temp_node, input_tree)
print(answer)

"""
5
1 5 1 -1
5 1 1 4 10 -1
4 3 10 5 10 -1
3 2 10 4 10 -1
2 3 10 -1
"""
