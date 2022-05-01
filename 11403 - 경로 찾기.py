N = int(input())

numbers = [[0] * N for _ in range(N)]
adj_lst = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j]:
            adj_lst[i].append(j)

for to in range(N):
    queue = adj_lst[to]
    head = 0
    rear = len(adj_lst[to])

    while head < rear:
        start = queue[head]
        head += 1

        for finish in adj_lst[start]:
            if finish in queue:
                continue

            queue.append(finish)
            rear += 1

    for go in queue:
        numbers[to][go] = 1

for number in numbers:
    print(*number)
