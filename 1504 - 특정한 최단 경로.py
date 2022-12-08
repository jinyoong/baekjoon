import sys
from heapq import *

custom_input = sys.stdin.readline

N, E = map(int, custom_input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, custom_input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, custom_input().split())


def solution(n, node1, node2):
    node1_to_node2 = dijkstra(node1, node2, n)

    start_to_node1 = dijkstra(1, node1, n)
    node2_to_end = dijkstra(node2, n, n)
    result1 = start_to_node1 + node1_to_node2 + node2_to_end

    start_to_node2 = dijkstra(1, node2, n)
    node1_to_end = dijkstra(node1, n, n)
    result2 = start_to_node2 + node1_to_node2 + node1_to_end

    answer = result1 if result1 < result2 else result2

    if answer >= 10 ** 18:
        return -1

    return answer


def dijkstra(start, goal, n):
    result = [10 ** 18] * (n + 1)
    result[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        total_line, current = heappop(heap)

        if total_line > result[current]:
            continue

        if current == goal:
            break

        for next_node, line in graph[current]:
            temp_line = total_line + line

            if temp_line >= result[next_node]:
                continue

            result[next_node] = temp_line
            heappush(heap, (temp_line, next_node))

    return result[goal]


print(solution(N, v1, v2))


"""
4 5
1 2 3
1 3 1
1 4 1
2 3 3
3 4 4
2 3

7 7
1 2 3
3 2 5
1 3 1
6 5 3
7 5 8
5 4 2
6 4 3
2 6
"""