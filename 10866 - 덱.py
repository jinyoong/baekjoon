import sys

N = int(input())
deque = [0] * N
head = 0
rear = 0
answers = []

for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        head -= 1
        deque[head] = command[1]

    elif command[0] == 'push_back':
        deque[rear] = command[1]
        rear += 1

    elif command[0] == 'pop_front':
        if head >= rear:
            answers.append(-1)
        else:
            answers.append(deque[head])
            head += 1

    elif command[0] == 'pop_back':
        if head >= rear:
            answers.append(-1)
        else:
            answers.append(deque[rear-1])
            rear -= 1

    elif command[0] == 'size':
        answers.append(rear - head)

    elif command[0] == 'empty':
        if head >= rear:
            answers.append(1)
        else:
            answers.append(0)

    elif command[0] == 'front':
        if head >= rear:
            answers.append(-1)
        else:
            answers.append(deque[head])

    else:
        if head >= rear:
            answers.append(-1)
        else:
            answers.append(deque[rear-1])

for answer in answers:
    print(answer)
