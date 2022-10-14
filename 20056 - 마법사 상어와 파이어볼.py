import sys

custom_input = sys.stdin.readline

N, M, K = map(int, custom_input().split())
numbers = [[[] for _ in range(N)] for _ in range(N)]
input_set = set()
for _ in range(M):
    r, c, m, s, d = map(int, custom_input().split())
    numbers[r - 1][c - 1].append([m, s, d])
    input_set.add((r - 1, c - 1))
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def solution(n, k, board, fireballs):
    answer = 0

    for _ in range(k):
        new_fireballs = set()
        new_board = [[[] for _ in range(N)] for _ in range(N)]

        # print(f"이동 전 파이어볼의 좌표들 : {fireballs}")
        # print(f"이동 전 파이어볼의 정보들 : {board}")

        for fireball in fireballs:
            fr, fc = fireball

            for ele in board[fr][fc]:

                fm, fs, fd = ele
                nr, nc = (fr + direction[fd][0] * fs) % n, (fc + direction[fd][1] * fs) % n

                new_fireballs.add((nr, nc))
                new_board[nr][nc].append([fm, fs, fd])

        new_new_fireballs = set()
        new_new_board = [[[] for _ in range(n)] for _ in range(n)]

        for new_fireball in new_fireballs:

            nfr, nfc = new_fireball

            if len(new_board[nfr][nfc]) == 1:
                new_new_fireballs.add((nfr, nfc))
                new_new_board[nfr][nfc] = new_board[nfr][nfc]
                continue

            total_m = 0
            total_s = 0
            is_odd = set()

            for i in range(len(new_board[nfr][nfc])):

                nfm, nfs, nfd = new_board[nfr][nfc][i]
                total_m += nfm
                total_s += nfs
                is_odd.add(nfd % 2)

            nm = total_m // 5
            ns = total_s // len(new_board[nfr][nfc])

            if len(is_odd) == 1:
                total_d = [0, 2, 4, 6]
            else:
                total_d = [1, 3, 5, 7]

            if nm == 0:
                continue

            for i in total_d:

                new_new_board[nfr][nfc].append([nm, ns, i])
                new_new_fireballs.add((nfr, nfc))

        fireballs = new_new_fireballs
        board = new_new_board[:][:]
        # print(f"새로운 파이어볼의 좌표들 : {fireballs}")
        # print(f"새로운 파이어볼의 정보들 : {board}")

    for row in range(n):
        for col in range(n):

            if not board[row][col]:
                continue

            for bm, bs, bd in board[row][col]:
                answer += bm

    return answer


print(solution(N, K, numbers, input_set))
