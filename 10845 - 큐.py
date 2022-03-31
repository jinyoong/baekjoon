import sys

N = int(input())

queue = []

for _ in range(N):
    commands = list(sys.stdin.readline().split())
    if commands[0] == 'push':
        queue.append(commands[1])
    elif commands[0] == 'pop':
        if queue:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        print(0) if queue else print(1)
    elif commands[0] == 'front':
        print(queue[0]) if queue else print(-1)
    else:
        print(queue[-1]) if queue else print(-1)
