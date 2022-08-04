N, M, X = map(int, input().split())
roads = [[0] * (N + 1) for _ in range(N + 1)]
students = [0] * (N + 1)

for _ in range(M):
    s, f, t = map(int, input().split())
    roads[s][f] = t


def back(start):
    result = [987654321] * (N + 1)
    result[start] = 0
    queue = [(start, 0)]
    idx = 0
    length = 1

    while idx < length:
        current, time = queue[idx]
        idx += 1

        if result[current] < time:
            continue

        for node, cost in enumerate(roads[current]):
            if not cost:
                continue

            if node == current or node == start:
                continue

            new_time = time + cost
            if result[node] > new_time:
                result[node] = new_time
                queue.append((node, new_time))
                length += 1

    return result


answer = back(X)
for i in range(1, N + 1):
    if i != X:
        answer[i] += back(i)[X]
print(max(answer[1:]))
