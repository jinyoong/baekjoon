N = int(input())

fish = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_shark():
    for i in range(N):
        for j in range(N):
            if fish[i][j] == 9:
                return [i, j]


start = find_shark()

while True:
    check = [[0] * N for _ in range(N)]
    cnt = 0
    sr, sc = start
    queue = [[(sr, sc), 0]]
    head = 0
    rear = 1

    while head < rear:
        loc, d = queue[head]
        r, c = loc

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue



