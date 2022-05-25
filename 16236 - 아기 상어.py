N = int(input())

fish = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_shark():
    for i in range(N):
        for j in range(N):
            if fish[i][j] == 9:
                return [i, j, 2]


def select_fish(foods):
    result = sorted(foods, key=lambda x: (x[0], x[1]))
    return result[0]


def move_shark(sr, sc, shark):
    check = {(sr, sc), }
    queue = [(sr, sc, 0)]
    head = 0
    rear = 1

    min_time = 987654321
    food = []

    while head < rear:
        r, c, time = queue[head]
        head += 1

        for i in range(4):
            nr, nc, new_time = r + dr[i], c + dc[i], time + 1

            if (nr, nc) in check:
                continue

            if new_time > min_time:
                continue

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if fish[nr][nc] > shark:
                continue

            if fish[nr][nc] < shark and fish[nr][nc]:
                check.add((nr, nc))
                if new_time < min_time:
                    food = [(nr, nc, new_time)]
                    min_time = new_time
                else:
                    food.append((nr, nc, new_time))
                    min_time = new_time
                continue

            queue.append((nr, nc, new_time))
            check.add((nr, nc))
            rear += 1

    if not food:
        return [-1, -1, -1]

    next_position = select_fish(food)

    return next_position


start = find_shark()
fish[start[0]][start[1]] = 0
answer = 0
cnt = 0

while True:
    start_r, start_c, start_power = start
    arrive_r, arrive_c, arrive_time = move_shark(start_r, start_c, start_power)

    if arrive_r == -1:
        print(answer)
        break

    if arrive_r != -1:
        fish[arrive_r][arrive_c] = 0
        cnt += 1

    if cnt == start_power:
        start_power += 1
        cnt = 0

    start = [arrive_r, arrive_c, start_power]
    answer += arrive_time



