def make_element(input_str):
    return [int(input_str), 0]


N, M, k = map(int, input().split())
board = [list(map(make_element, input().split())) for _ in range(N)]
next_sharks = [[-1, -1] for _ in range(M + 1)]
sharks_direction_lst = [0] + list(map(int, input().split()))
sharks = [[-1, -1] for _ in range(M + 1)]
direction_lst = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
direction_priority = [[]]  # 1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽

for _ in range(M):
    direction_priority.append([[]] + [list(map(int, input().split())) for _ in range(4)])

for r in range(N):
    for c in range(N):
        if board[r][c][0]:
            sharks[board[r][c][0]] = [r, c]
            board[r][c][1] = k

answer = 0

while answer <= 1000:

    if sharks.count([-1, -1]) == M:
        break

    answer += 1

    for idx in range(1, M + 1):  # 상어 번호에 따라 방향 우선순위에 맞춰 이동
        if sharks[idx] == [-1, -1]:
            continue

        current_r, current_c = sharks[idx]
        current_d = sharks_direction_lst[idx]
        shark_direction = direction_priority[idx]

        for next_direction in shark_direction[current_d]:
            nr, nc = current_r + direction_lst[next_direction][0], current_c + direction_lst[next_direction][1]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if 0 < board[nr][nc][1] < k:
                continue

            if board[nr][nc][1] == k + 1:
                sharks[idx] = [-1, -1]
                break

            sharks[idx] = [nr, nc]
            sharks_direction_lst[idx] = next_direction
            board[nr][nc] = [idx, k + 1]
            break

        else:
            for next_direction in shark_direction[current_d]:
                nr, nc = current_r + direction_lst[next_direction][0], current_c + direction_lst[next_direction][1]

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                if board[nr][nc][0] != idx:
                    continue

                next_sharks[idx] = [nr, nc]
                sharks_direction_lst[idx] = next_direction
                break

    for idx in range(1, M + 1):
        if next_sharks[idx] != [-1, -1]:
            sharks[idx] = next_sharks[idx]
            board[next_sharks[idx][0]][next_sharks[idx][1]][1] = k + 1
            next_sharks[idx] = [-1, -1]

    for r in range(N):
        for c in range(N):
            if board[r][c][1] != 0:
                board[r][c][1] -= 1

                if board[r][c][1] == 0:
                    board[r][c] = [0, 0]

if answer > 1000:
    print(-1)
else:
    print(answer)
