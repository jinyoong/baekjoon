import sys


def solution(node_count, target):
    # 1번 정점을 먼저 0번 집합에 넣은 뒤 너비우선탐색으로 보며 인접한 점들을 1번 집합에 담아넣는다
    # 그 다음 정점에서 너비우선탐색으로 본 인접한 점들은 집합 0에 넣어야 한다
    # 이 때 집합 0에 이미 들어가 있는 점과 인접한 경우가 있으면 이분그래프가 되지 않는다

    visited = {1, }
    lst = [{1, }, set()]
    queue = [(0, 1)]
    idx = 0
    length = 1

    while idx < length:
        current_lst_idx, current_node = queue[idx]
        idx += 1

        for next_node in target[current_node]:

            if next_node in visited:
                continue

            visited.add(next_node)
            next_lst_idx = (current_lst_idx + 1) % 2

            for temp_node in lst[next_lst_idx]:
                if next_node in target[temp_node]:
                    return "No"
            else:
                queue.append((next_lst_idx, next_node))
                lst[next_lst_idx].add(next_node)
                length += 1

        if idx == length and len(visited) != node_count:
            for k in range(1, node_count + 1):

                if k in visited:
                    continue

                queue.append((current_lst_idx, k))
                lst[current_lst_idx].add(k)
                visited.add(k)
                length += 1
                break

    return "YES"


def solution2(node_count, target_graph):
    # solution1 의 과정을 좀 더 간단하게 변경
    visited = [-1] * (node_count + 1)
    visited[1] = 0
    count = 1
    queue = [1]
    idx = 0
    length = 1

    while idx < length:
        current_node = queue[idx]
        current_set = visited[current_node]  # current_node 가 속해있는 집합 번호
        next_set = (current_set + 1) % 2  # current_node 와 인접한 노드들이 들어가야 할 집합 번호
        idx += 1

        for next_node in target_graph[current_node]:

            if visited[next_node] == visited[current_node]:  # next_node 가 current_node 집합에 들어있는 경우 이분그래프 X
                return "NO"

            if visited[next_node] != -1:
                continue

            visited[next_node] = next_set  # 반대 집합에 next_node 를 넣어준다
            queue.append(next_node)
            count += 1
            length += 1

        if idx == length and count != node_count:  # 그래프가 서로 떨어져있는 경우 다른 노드부터 살펴보기 위한 반복문
            for new_node in range(1, node_count + 1):
                if visited[new_node] == -1:
                    queue.append(new_node)
                    visited[new_node] = next_set
                    count += 1
                    length += 1
                    break

    return "YES"


K = int(input())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [set() for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].add(v)
        graph[v].add(u)

    print(solution2(V, graph))

'''
1
4 4
1 2
2 3
3 4
4 2

1
5 4
1 2
3 4
3 5
4 5

1
6 3
1 2
3 4
5 6
'''
