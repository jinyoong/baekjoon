T = int(input())

for _ in range(T):
    l, n = map(int, input().split())
    position = [0 for _ in range(l)]
    for _ in range(n):
        p = int(input())
        position[p] = 1

