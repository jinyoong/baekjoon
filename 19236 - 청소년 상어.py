import sys

custom_input = sys.stdin.readline

board = [[[0, 0] for _ in range(4)] for _ in range(4)]
lst = [[0, 0] for _ in range(17)]
for i in range(4):
    numbers = list(map(int, custom_input().split()))
    for j in range(0, 8, 2):
        board[i][j // 2] = [numbers[j], numbers[j + 1] - 1]
        lst[numbers[j]] = [i, j // 2]

direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]


def solution(first_field, first_number):
    answer = 0
    shark = [0, 0, first_field[0][0][1], first_field[0][0][0]]
    first_number[first_field[0][0][0]] = [-1, -1]
    first_field[0][0] = [-2, -2]

    def move(shark_info, field, number, level):
        nonlocal answer
        sr, sc, sd, result = shark_info

        for fish in range(1, 17):

            if number[fish] == [-1, -1]:
                continue

            r, c = number[fish]
            d = field[r][c][1]

            for k in range(7):
                new_d = (d + k) % 8
                nr, nc = r + direction[new_d][0], c + direction[new_d][1]

                if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                    continue

                if field[nr][nc] == [-2, -2]:
                    continue

                change_fish = field[nr][nc][0]
                field[r][c] = field[nr][nc][:]
                field[nr][nc] = [fish, new_d]
                number[fish] = [nr, nc]
                if field[nr][nc] != [-1, -1]:
                    number[change_fish] = [r, c]
                break

        for k in range(1, 4):
            nsr, nsc = sr + direction[sd][0] * k, sc + direction[sd][1] * k

            if nsr < 0 or nsr >= 4 or nsc < 0 or nsc >= 4:
                if k == 1:
                    if result > answer:
                        answer = result
                return

            new_field = [[[0, 0] for _ in range(4)] for _ in range(4)]
            for r in range(4):
                for c in range(4):
                    new_field[r][c][0], new_field[r][c][1] = field[r][c][0], field[r][c][1]

            new_number = [number[k][:] for k in range(17)]
            new_field[sr][sr] = [-1, -1]

            target_fish = new_field[nsr][nsc][:]
            new_field[nsr][nsc] = [-2, -2]
            new_number[target_fish[0]] = [-1, -1]
            move([nsr, nsc, target_fish[1], result + target_fish[0]], new_field, new_number, level + 1)

    move(shark, first_field, first_number, 0)

    return answer


print(solution(board, lst))
