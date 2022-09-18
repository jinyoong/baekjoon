N = int(input())
table = [[] for _ in range(N ** 2 + 1)]
board = [[0] * N for _ in range(N)]
students = []

for _ in range(N ** 2):
    numbers = list(map(int, input().split()))
    student, friends = numbers[0], numbers[1:]
    table[student] = friends
    students.append(student)


def solution():
    """
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    """
    answer = 0
    points = [0, 1, 10, 100, 1000]
    board[1][1] = students[0]  # 3번 조건에 의해 맨 첫 학생은 (1, 1) 위치에 올 수 밖에 없다.
    next_position_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(1, N ** 2):
        next_student = students[i]
        can_position = []
        max_friends_count = 0

        for r in range(N):
            for c in range(N):

                if board[r][c]:
                    continue

                count = 0
                for j in range(4):
                    nr, nc = r + next_position_lst[j][0], c + next_position_lst[j][1]

                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue

                    if board[nr][nc] in table[next_student]:
                        count += 1

                if max_friends_count < count:
                    can_position = [(r, c)]
                    max_friends_count = count
                elif max_friends_count == count:
                    can_position.append((r, c))
                else:
                    continue

        if len(can_position) == 1:
            next_r, next_c = can_position[0]
            board[next_r][next_c] = next_student
            continue

        can_position_second = []
        max_blank_count = 0
        for pass_first in can_position:
            r, c = pass_first
            blank_count = 4

            for j in range(4):
                nr, nc = r + next_position_lst[j][0], c + next_position_lst[j][1]

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    blank_count -= 1
                    continue

                if board[nr][nc]:
                        blank_count -= 1

            if max_blank_count < blank_count:
                can_position_second = [(r, c)]
                max_blank_count = blank_count
            elif max_blank_count == blank_count:
                can_position_second.append((r, c))
            else:
                continue

        next_r, next_c = can_position_second[0]
        board[next_r][next_c] = next_student

    for r in range(N):
        for c in range(N):
            count = 0

            for j in range(4):
                nr, nc = r + next_position_lst[j][0], c + next_position_lst[j][1]

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                if board[nr][nc] in table[board[r][c]]:
                    count += 1

            answer += points[count]

    return answer


print(solution())
