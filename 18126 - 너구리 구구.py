N = int(input())

rooms = [[] for _ in range(N+1)]

for _ in range(N-1):
     a, b, c = map(int, input().split())
     rooms[a].append((b, c))
     rooms[b].append((a, c))

check = {1, }
queue = [1]
head = 0
rear = 1
distance = [0] * (N+1)

while head < rear:
    parents = queue[head]
    d = distance[parents]
    head += 1

    for ele in rooms[parents]:
        child, line = ele
        if child in check:
            continue

        check.add(child)
        distance[child] = d + line
        queue.append(child)
        rear += 1

print(max(distance))
