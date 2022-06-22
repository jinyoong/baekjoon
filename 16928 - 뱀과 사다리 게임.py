N, M = map(int, input().split())
up_down = [0 for _ in range(101)]
check = [0 for _ in range(101)]
for _ in range(N + M):
    start, finish = map(int, input().split())
    up_down[start] = finish

queue = [(1, 0)]
check[1] = 1
head = 0

while True:
    start, count = queue[head]
    head += 1

    if start == 100:
        print(count)
        break

    for i in range(6, 0, -1):
        arrive = start + i

        if arrive > 100:
            continue

        if check[arrive]:
            continue

        pipe = up_down[arrive]

        if pipe:

            if check[pipe]:
                continue

            queue.append((pipe, count + 1))
            check[pipe] = 1
        else:
            queue.append((arrive, count + 1))
            check[arrive] = 1
