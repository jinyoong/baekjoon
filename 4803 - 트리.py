import sys

custom_input = sys.stdin.readline


def is_graph(current, before):
    global is_tree

    if current in visited:
        is_tree = False
        return

    visited.add(current)

    for next_node in graph[current]:

        if next_node == before:
            continue

        is_graph(next_node, current)


case = 0

while True:
    case += 1
    n, m = map(int, custom_input().split())
    graph = [[] for _ in range(n + 1)]

    if n == m == 0:
        break

    for _ in range(m):
        a, b = map(int, custom_input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    count = 0

    for i in range(1, n + 1):
        is_tree = True

        if i in visited:
            continue

        is_graph(i, -1)

        if is_tree:
            count += 1

    if count == 0:
        print("Case {}: No trees.".format(case))
    elif count == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, count))

"""
7 7
1 2
2 3
3 1
4 5
5 6
6 4
1 6
0 0

6 7
1 2
1 3
1 4
2 3
2 4
3 4
5 6
0 0
"""
