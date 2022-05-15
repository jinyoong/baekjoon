t = int(input())

for _ in range(t):
    n = int(input())
    n += 2

    points = [list(map(int, input().split())) for _ in range(n)]

    queue = [0]
    check = {0, }
    head = 0
    rear = 1
    answer = ""

    while head < rear:
        s_idx = queue[head]
        s_x, s_y = points[s_idx]
        head += 1

        for g_idx in range(n):

            if g_idx in check:
                continue

            g_x, g_y = points[g_idx]
            distance = abs(s_x - g_x) + abs(s_y - g_y)

            if distance <= 1000:
                check.add(g_idx)
                queue.append(g_idx)
                rear += 1

        if n - 1 in check:
            answer = "happy"
            break

    if n - 1 not in check:
        answer = "sad"

    print(answer)

"""
1
2
0 0
-450 -250
-600 500
-600 1000

3
0
1000 1000
1000 1001
1
0 0
1000 0
0 2000
2
0 0
10000 0
0 1000
0 2000
"""
