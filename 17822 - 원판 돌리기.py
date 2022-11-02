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
    new_circle = [[0] * m for _ in range(n)]

    is_adj = False
    total = 0
    count = 0
    for r in range(n):
        total += sum(circle[r])
        visited = set()
        for c in range(m):
            if not circle[r][c]:
                continue

            count += 1

            if c in visited:
                continue

            if circle[r][c] == circle[r][(c + 1) % m]:
                is_adj = True
                new_circle[r][c] = new_circle[r][(c + 1) % m] = 0
                visited.add(c)
                visited.add(c + 1)
            else:
                new_circle[r][c] = circle[r][c]

    circle = [new_circle[r][:] for r in range(n)]

    for c in range(m):
        visited = set()
        for r in range(n):

            if r in visited:
                continue

            if r == n - 1:
                if not circle[r][c]:
                    continue

                if circle[r][c] != circle[r - 1][c]:
                    new_circle[r][c] = circle[r][c]
            else:
                if not circle[r][c]:
                    continue

                if circle[r][c] == circle[r + 1][c]:
                    new_circle[r][c] = new_circle[r + 1][c] = 0
                    is_adj = True
                    visited.add(r)
                    visited.add(r + 1)
                else:
                    new_circle[r][c] = circle[r][c]

    if is_adj:
       return new_circle

    average = total / count
    for r in range(n):
        for c in range(m):
            if not circle[r][c]:
                continue

            if circle[r][c] < average:
                new_circle[r][c] = circle[r][c] + 1
            elif circle[r][c] > average:
                new_circle[r][c] = circle[r][c] - 1

    return new_circle


def solution(circle, orders, n, m):
    answer = 0

    for order in orders:
        rotate_circle = rotate(circle, order[0], order[1], order[2], n, m)
        change_circle = change_number(rotate_circle, n, m)
        circle = [change_circle[i][:] for i in range(n)]

    for r in range(n):
        answer += sum(circle[r])
    print(circle)
    return answer


print(solution(numbers, lst, N, M))
