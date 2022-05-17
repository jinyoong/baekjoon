import sys

N = int(input())

friends = [[] for _ in range(N + 1)]
tree = [0] * (N + 1)

for _ in range(N - 1):
    i, j = map(int, sys.stdin.readline().split())
    friends[i].append(j)
    friends[j].append(i)

print(friends)

answer = 0
queue = []
head = 0
rear = 0

for friend in friends:
    if len(friend) == 1 and not tree[friend[0]]:
        tree[friend[0]] = 1
        queue.append(friend[0])
        rear += 1

print(queue)
print(tree)

while head < rear:
    node = queue[head]
    head += 1


