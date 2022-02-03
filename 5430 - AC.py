N = int(input())

for _ in range(N):
    commands = input().strip()
    cnt = int(input())
    target = input()[1:-1].split(',')

    head = 0
    rear = cnt - 1
    is_reverse = False
    is_break = False

    for command in commands:
        if command == 'R':
            is_reverse = not is_reverse

        else:
            if head > rear:
                is_break = True
                break

            if is_reverse:
                rear -= 1
            else:
                head += 1

    if is_break:
        print('error')
        continue

    if is_reverse:
        print('[', end="")
        for i in range(rear, head-1, -1):
            if i == head:
                print(int(target[i]), end="")
            else:
                print(int(target[i]), end=",")
        print(']')

    else:
        print('[', end="")
        for i in range(head, rear+1):
            if i == rear:
                print(int(target[i]), end="")
            else:
                print(int(target[i]), end=",")
        print(']')
