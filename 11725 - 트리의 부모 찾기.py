import sys


N = int(input())
tree = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1][n2] = tree[n2][n1] = 1

parents = {}

queue = [1] * (2 * N)
check = {1, }
head = 0
rear = 1

while head < rear:
    parent = queue[head]
    head += 1

    for i in range(N+1):
        if not tree[parent][i]:
            continue

        child = i

        if child not in check:
            parents[child] = parent
            queue[rear] = child
            check.add(child)
            rear += 1

for node in range(2, N+1):
    print(parents[node])
