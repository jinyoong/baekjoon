N, M = map(int, input().split())

# python3 으로만 돌려본 코드, 실패

result = [set()]

for _ in range(M):
    a, b = map(int, input().split())
    is_in_a = is_in_b = 0
    for i in range(len(result)):
        if a in result[i]:
            is_in_a = i

        if b in result[i]:
            is_in_b = i

        if is_in_a and is_in_b:
            break

    if is_in_a == 0 and is_in_b == 0:
        result.append({a, b})
        continue

    if is_in_a == is_in_b:
        continue

    if is_in_a and is_in_b:
        result[is_in_a].union(result[is_in_b])
        result.pop(is_in_b)
        continue

    if is_in_a:
        result[is_in_a].add(b)
        continue

    if is_in_b:
        result[is_in_b].add(a)
        continue

print(len(result) - 1)

# python3 시간초과(실패), pypy3 성공

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

nodes = [0] * (N + 1)
nodes[0] = 1
answer = 0

for i in range(1, N + 1):
    if nodes[i]:
        continue

    answer += 1
    queue = [i]
    head = 0
    rear = 1

    while head < rear:
        node = queue[head]
        targets = list(graph[node])
        head += 1

        for target in targets:
            if nodes[target]:
                continue

            nodes[target] = 1
            queue.append(target)
            rear += 1

print(answer)
