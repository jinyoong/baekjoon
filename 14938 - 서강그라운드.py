import sys

n, m, r = map(int, sys.stdin.readline().split())
items = [0] + list(map(int, sys.stdin.readline().split()))
lines = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    lines[a][b] = lines[b][a] = l


def get_item(start_point, game_map, limit, total, item_map):

    result = item_map[start_point]
    visited = [987654321] * (total + 1)
    visited[start_point] = 0
    queue = [start_point]
    idx = 0
    length = 1

    while idx < length:
        current_point = queue[idx]
        current_line = visited[current_point]
        idx += 1

        for next_point, line in enumerate(game_map[current_point]):

            if line == 0:
                continue

            new_line = line + current_line

            if visited[next_point] < new_line:
                continue

            if new_line > limit:
                continue

            if visited[next_point] == 987654321:
                result += item_map[next_point]

            visited[next_point] = new_line
            queue.append(next_point)
            length += 1

    return result


answer = 0

for i in range(1, n + 1):
    point = get_item(i, lines, m, n, items)
    if answer < point:
        answer = point

print(answer)
