N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 북동남서 순서
board = [list(map(int, input().split())) for _ in range(N)]


def solution(robot, direction, room):
    answer = 0
    direction_lst = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [robot]
    idx = 0
    length = 1

    while idx < length:
        current_r, current_c = queue[idx]
        idx += 1

        if room[current_r][current_c] != 2:
            answer += 1
            room[current_r][current_c] = 2

        for _ in range(4):
            next_direction = (direction + 3) % 4
            next_r, next_c = current_r + direction_lst[next_direction][0], current_c + direction_lst[next_direction][1]

            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue

            if room[next_r][next_c] == 0:
                direction = next_direction
                queue.append((next_r, next_c))
                length += 1
                break

            if room[next_r][next_c] != 0:
                direction = next_direction
                continue

        else:  # 네 방향이 모두 청소가 되어있거나 벽인 경우
            back_direction = (direction + 2) % 4
            back_r, back_c = current_r + direction_lst[back_direction][0], current_c + direction_lst[back_direction][1]

            if room[back_r][back_c] == 1:
                return answer
            else:
                queue.append((back_r, back_c))
                length += 1


print(solution((r, c), d, board))
