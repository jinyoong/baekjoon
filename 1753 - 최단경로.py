import sys
from heapq import heappush, heappop

custom_input = sys.stdin.readline

V, E = map(int, custom_input().split())
K = int(custom_input())
nodes = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, custom_input().split())

    nodes[u].append([v, w])


def solution(start, total):

    answer = [987654321] * (total + 1)
    answer[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        result, current = heappop(queue)

        if answer[current] < result:
            continue

        for node, weight in nodes[current]:

            new_result = result + weight

            if new_result < answer[node]:
                answer[node] = new_result
                heappush(queue, (new_result, node))

    return answer


answer_lst = solution(K, V)

for i in range(1, V + 1):

    if answer_lst[i] == 987654321:
        print("INF")
    else:
        print(answer_lst[i])
