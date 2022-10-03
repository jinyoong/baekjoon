N = int(input())
K = int(input())
apples = {tuple(map(int, input().split())) for _ in range(K)}
L = int(input())
commands = {}

for _ in range(L):
    X, C = input().split()
    commands[int(X)] = C

d_idx = 0
direction_lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0
snake = [(1, 1)]

while True:
    time += 1
    head_r, head_c = snake[-1]
    new_head_r, new_head_c = head_r + direction_lst[d_idx][0], head_c + direction_lst[d_idx][1]

    if new_head_r < 1 or new_head_r > N or new_head_c < 1 or new_head_c > N:
        break

    if (new_head_r, new_head_c) in snake:
        break

    if (new_head_r, new_head_c) in apples:
        apples.remove((new_head_r, new_head_c))
    else:
        snake.pop(0)

    snake.append((new_head_r, new_head_c))

    if time in commands.keys():
        if commands[time] == "L":
            d_idx = (d_idx + 3) % 4
        else:
            d_idx = (d_idx + 1) % 4

print(time)
