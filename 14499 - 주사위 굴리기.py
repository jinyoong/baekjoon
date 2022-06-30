N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [1, 2, 3, 4, 5, 6]  # 위, 앞, 아래, 뒤, 좌, 우


def down():
    before = dice[0]
    for i in range(1, 4):
        current = dice[i]
        dice[i] = before
        before = current
    dice[0] = before


def up():
    before = dice[3]
    for i in range(2, -1, -1):
        current = dice[i]
        dice[i] = before
        before = current
    dice[3] = before


def left():
    new_left, new_up, new_right, new_down = dice[0], dice[5], dice[2], dice[4]
    dice[0], dice[2], dice[4], dice[5] = new_up, new_down, new_left, new_right


def right():
    new_left, new_up, new_right, new_down = dice[2], dice[4], dice[0], dice[5]
    dice[0], dice[2], dice[4], dice[5] = new_up, new_down, new_left, new_right


def is_out(r, c, n, m):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    return True


for command in commands:

    if command == 1:
        y += 1
        if is_out(x, y, N, M):
            right()
        else:
            y -= 1
            continue
    elif command == 2:
        y -= 1
        if is_out(x, y, N, M):
            left()
        else:
            y += 1
            continue
    elif command == 3:
        x -= 1
        if is_out(x, y, N, M):
            up()
        else:
            x += 1
            continue
    else:
        x += 1
        if is_out(x, y, N, M):
            down()
        else:
            x -= 1
            continue

    number = maps[x][y]

    if number:
        dice[2] = number
        maps[x][y] = 0
        print(dice[0])
    else:
        maps[x][y] = dice[2]
        print(dice[0])
