import sys

t = int(input())

numbers = [0] * 21

for _ in range(t):
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'add':
        numbers[int(command[1])] = 1
    elif command[0] == 'remove':
        numbers[int(command[1])] = 0
    elif command[0] == 'check':
        if numbers[int(command[1])]:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        numbers[int(command[1])] = (numbers[int(command[1])] + 1) % 2
    elif command[0] == 'all':
        numbers = [1] * 21
    else:
        numbers = [0] * 21
