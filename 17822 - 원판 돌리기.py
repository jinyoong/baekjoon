import sys

custom_input = sys.stdin.readline

N, M, T = map(int, custom_input().split())
numbers = [list(map(int, custom_input().split())) for _ in range(N)]
lst = [list(map(int, custom_input().split())) for _ in range(T)]


def rotate(circle, x, d, k, n, m):
    idx = x - 1

    while idx < n:
        new_circle = [0] * m

        for i in range(m):

            if d == 0:
                new_circle[(i + k) % m] = circle[idx][i]
            else:
                new_circle[(i - k) % m] = circle[idx][i]

        circle[idx] = new_circle
        idx += x

    return circle


def change_number(circle, n, m):
    new_circle = [[-987654321] * m for _ in range(n)]
    is_change = False
    visited = set()

    for r in range(n):
        for c in range(m):

            if circle[r][c] == -987654321:
                continue

            if (r, c) in visited:
                continue

            queue = [(r, c)]
            visited.add((r, c))
            idx = 0
            length = 1

            while idx < length:
                sr, sc = queue[idx]
                idx += 1

                for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nr, nc = sr + d[0], (sc + d[1]) % m

                    if nr < 0 or nr >= n:
                        continue

                    if (nr, nc) in visited:
                        continue

                    if circle[nr][nc] != circle[sr][sc]:
                        continue

                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    is_change = True
                    length += 1

            if len(queue) == 1:
                new_circle[r][c] = circle[r][c]
                continue

            for ele in queue:
                qr, qc = ele
                new_circle[qr][qc] = -987654321

    if is_change:
        return new_circle

    total = count = 0
    for r in range(n):
        for c in range(m):

            if circle[r][c] == -987654321:
                continue
            total += circle[r][c]
            count += 1

    if count == 0:
        return new_circle

    average = total / count

    for r in range(n):
        for c in range(m):

            if circle[r][c] == -987654321:
                continue

            if circle[r][c] - average > 0.0:
                new_circle[r][c] = circle[r][c] - 1
            elif circle[r][c] - average == 0.0:
                new_circle[r][c] = circle[r][c]
            else:
                new_circle[r][c] = circle[r][c] + 1

    return new_circle


def solution(circle, orders, n, m):
    answer = 0

    for order in orders:
        rotate_circle = rotate(circle, order[0], order[1], order[2], n, m)
        change_circle = change_number(rotate_circle, n, m)
        circle = [change_circle[i][:] for i in range(n)]

    for r in range(n):
        for c in range(m):
            if circle[r][c] != -987654321:
                answer += circle[r][c]
    return answer


print(solution(numbers, lst, N, M))
