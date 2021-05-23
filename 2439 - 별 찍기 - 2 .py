T = int(input())

for i in range(T):
    print('{}{}'.format(' ' * (T - i -1), '*' * (i + 1)))