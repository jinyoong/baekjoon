N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

start = V
ans_bfs = []
ans_dfs = []
bfs_visited = set()
dfs_visited = set()


def bfs(graph, num):
    if num in bfs_visited:
        return
    bfs_visited.add(num)
    ans_bfs.append(num)
    nodes = sorted(graph[num])
    for i in nodes:
        bfs(graph, i)


def dfs(graph, nums):
    if not nums:
        return
    temp = []
    for num in nums:
        if num in dfs_visited:
            continue
        ans_dfs.append(num)
        dfs_visited.add(num)
        nodes = sorted(graph[num])
        temp += nodes
        # 처음에 모든 점들을 set 으로 묶어 오름차순 정렬했는데 틀렸다
        # 만약 다음 정점들이 [3, 4], [1, 2] 순으로 나왔다고 하면, dfs 방법으로는 3 => 4 => 1 => 2 순서여야 하는데
        # 내가 처음에 한 코드는 1 => 2 => 3 => 4 순서가 되서 틀렸던 것
    dfs(graph, temp)


bfs(graph, start)
dfs(graph, [start])

print(*ans_bfs)
print(*ans_dfs)
