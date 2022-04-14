import sys


def bfs(s, f):
    check = {s, }
    queue = [[s, 0]]
    head = 0
    rear = 1

    while head < rear:
        p, cnt = queue[head]
        head += 1
        if p == f:
            return cnt

        for ele in tree[p]:
            if ele in check:
                continue
            queue.append([ele, cnt+1])
            check.add(ele)
            rear += 1


N, M = map(int, sys.stdin.readline().split())
numbers = [[0] * (N+1) for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
answer = 0
minimum = 98765431

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    numbers[a][b] = numbers[b][a] = 1
    tree[a].append(b)
    tree[b].append(a)

for start in range(1, N+1):
    for last in range(1, N+1):
        if start == last:
            continue
        if numbers[start][last]:
            continue
        result = bfs(start, last)
        numbers[start][last] = numbers[last][start] = result

for i in range(1, N+1):
    if sum(numbers[i]) < minimum:
        minimum = sum(numbers[i])
        answer = i

print(answer)
