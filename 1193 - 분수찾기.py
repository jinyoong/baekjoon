N = int(input())

line = 0

for i in range(N):

    if line + i + 1 >= N:
        if (i + 1) % 2 == 1:
            print('{}/{}'.format(i + 2 - N + line, N - line))
        else:
            print('{}/{}'.format(N - line, i + 2 - N + line))
        break
    else:
        line += i + 1