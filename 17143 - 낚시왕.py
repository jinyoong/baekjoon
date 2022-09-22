import sys


def solution(sharks, width, height):
    direction_lst = [[], [-1, 0, 2], [1, 0, 1], [0, 1, 4], [0, -1, 3]]  # 2번 인덱스 자리의 숫자는 반대 방향의 번호
    answer = 0

    for i in range(width):
        # 낚시꾼이 오른쪽으로 이동 후 낚시 시도
        for h in range(height):

            if (h, i) in sharks:
                answer += sharks[(h, i)][2]
                del sharks[(h, i)]
                break

        # 남아있는 상어들을 이동
        new_sharks = {}
        for point, data in sharks.items():
            sr, sc = point
            speed, direction, size = data

            if direction <= 2:
                speed = speed % (height * 2 - 2)
            else:
                speed = speed % (width * 2 - 2)

            for k in range(speed):

                sr += direction_lst[direction][0]
                sc += direction_lst[direction][1]

                if sr < 0 or sr >= height or sc < 0 or sc >= width:
                    direction = direction_lst[direction][2]
                    sr += direction_lst[direction][0] * 2
                    sc += direction_lst[direction][1] * 2

            if (sr, sc) in new_sharks and size < new_sharks[(sr, sc)][2]:
                continue
            else:
                new_sharks[(sr, sc)] = (speed, direction, size)

        sharks = new_sharks

    return answer


R, C, M = map(int, sys.stdin.readline().split())
board = {}
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[(r - 1, c - 1)] = (s, d, z)

print(solution(board, C, R))
