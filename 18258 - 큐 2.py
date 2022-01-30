import sys

input = sys.stdin.readline

N = int(input())

queue = [0] * N
head = 0
rear = 0

for _ in range(N):
    command_lst = list(map(str, input().split()))
    command = command_lst[0]

    if command == 'push':
        queue[rear] = command_lst[1]
        rear += 1

    elif command == 'front':
        if head == rear:
            print(-1)
        else:
            print(queue[head])

    elif command == 'pop':
        if head == rear:
            print(-1)
        else:
            print(queue[head])
            head += 1

    elif command == 'size':
        print(rear - head)

    elif command == 'empty':
        if rear == head:
            print(1)
        else:
            print(0)

    elif command == 'back':
        if rear == head:
            print(-1)
        else:
            print(queue[rear-1])
